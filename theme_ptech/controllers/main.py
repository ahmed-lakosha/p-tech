from odoo import http, tools, fields
from odoo.addons.website.controllers.main import Website
from odoo.addons.website_blog.controllers.main import WebsiteBlog
from odoo.http import request


class WebsitePtech(Website):
    def index(self, **kw):
        current_website = http.request.website
        active_theme = current_website.theme_id

        if active_theme and active_theme.name == 'theme_ptech':
            company_id = http.request.env.company.id
            domain = [('company_id', '=', company_id)]
            service_ids = http.request.env['website.services'].sudo().search(domain, order='sequence asc')
            partner_ids = http.request.env['website.partners'].sudo().search(domain, order='sequence asc')
            app_ids = http.request.env['blog.post'].sudo().search([('is_app', '=', True)], order='sequence asc')

            data = {
                'service_ids': service_ids,
                'partner_ids': partner_ids,
                'app_ids': app_ids,
            }
            print(data)
            return http.request.render('website.homepage', data)
        else:
            return super(WebsitePtech, self).index(**kw)


class WebsiteServices(http.Controller):

    @http.route('/services', auth="public", website=True, sitemap=True)
    def services(self, **kw):
        company_id = http.request.env.company.id
        domain = [('company_id', '=', company_id)]
        service_ids = http.request.env['website.services'].sudo().search(domain)
        print(service_ids)

        data = {
            'service_ids': service_ids,
        }
        return http.request.render('theme_ptech.custom_services_page_template', data)


class CustomWebsiteBlog(WebsiteBlog):

    def _prepare_blog_values(self, blogs, blog=False, date_begin=False, date_end=False, tags=False, state=False,
                             page=False, search=None, **post):
        """ Prepare all values to display the blogs index page or one specific blog"""
        BlogPost = request.env['blog.post']
        BlogTag = request.env['blog.tag']

        # prepare domain
        domain = request.website.website_domain()

        if blog:
            domain += [('blog_id', '=', blog.id)]

        if date_begin and date_end:
            domain += [("post_date", ">=", date_begin), ("post_date", "<=", date_end)]
        active_tag_ids = tags and [request.env['ir.http']._unslug(tag)[1] for tag in tags.split(',')] or []
        active_tags = BlogTag
        if active_tag_ids:
            active_tags = BlogTag.browse(active_tag_ids).exists()
            fixed_tag_slug = ",".join(request.env['ir.http']._slug(t) for t in active_tags)
            if fixed_tag_slug != tags:
                path = request.httprequest.full_path
                new_url = path.replace("/tag/%s" % tags, fixed_tag_slug and "/tag/%s" % fixed_tag_slug or "", 1)
                if new_url != path:  # check that really replaced and avoid loop
                    return request.redirect(new_url, 301)
            domain += [('tag_ids', 'in', active_tags.ids)]

        if request.env.user.has_group('website.group_website_designer'):
            count_domain = domain + [("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())]
            published_count = BlogPost.search_count(count_domain)
            unpublished_count = BlogPost.search_count(domain) - published_count

            if state == "published":
                domain += [("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())]
            elif state == "unpublished":
                domain += ['|', ("website_published", "=", False), ("post_date", ">", fields.Datetime.now())]
        else:
            domain += [("post_date", "<=", fields.Datetime.now())]

        offset = (page - 1) * self._blog_post_per_page

        options = self._get_blog_post_search_options(
            blog=blog,
            active_tags=active_tags,
            date_begin=date_begin,
            date_end=date_end,
            state=state,
            **post
        )
        total, details, fuzzy_search_term = request.website._search_with_fuzzy("blog_posts_only", search,
                                                                               limit=page * self._blog_post_per_page,
                                                                               order="sequence asc",
                                                                               options=options)
        posts = details[0].get('results', BlogPost)
        posts = posts[offset:offset + self._blog_post_per_page]

        url_args = dict()
        if search:
            url_args["search"] = search

        if date_begin and date_end:
            url_args["date_begin"] = date_begin
            url_args["date_end"] = date_end

        pager = tools.lazy(lambda: request.website.pager(
            url=request.httprequest.path.partition('/page/')[0],
            total=total,
            page=page,
            step=self._blog_post_per_page,
            url_args=url_args,
        ))

        if not blogs:
            all_tags = request.env['blog.tag']
        else:
            all_tags = tools.lazy(lambda: blogs.all_tags(join=True) if not blog else blogs.all_tags().get(blog.id,
                                                                                                          request.env[
                                                                                                              'blog.tag']))
        tag_category = tools.lazy(
            lambda: sorted(all_tags.mapped('category_id'), key=lambda category: category.name.upper()))
        other_tags = tools.lazy(
            lambda: sorted(all_tags.filtered(lambda x: not x.category_id), key=lambda tag: tag.name.upper()))
        nav_list = tools.lazy(self.nav_list)
        # and avoid accessing related blogs one by one
        posts.blog_id

        return {
            'date_begin': date_begin,
            'date_end': date_end,
            'other_tags': other_tags,
            'tag_category': tag_category,
            'nav_list': nav_list,
            'tags_list': self.tags_list,
            'pager': pager,
            'posts': posts.with_prefetch(),
            'tag': tags,
            'active_tag_ids': active_tags.ids,
            'domain': domain,
            'state_info': state and {"state": state, "published": published_count, "unpublished": unpublished_count},
            'blogs': blogs,
            'blog': blog,
            'search': fuzzy_search_term or search,
            'search_count': total,
            'original_search': fuzzy_search_term and search,
        }
