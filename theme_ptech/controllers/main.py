from odoo import http
from odoo.addons.website.controllers.main import Website


class WebsitePtech(Website):
    def index(self, **kw):
        current_website = http.request.website
        active_theme = current_website.theme_id

        if active_theme and active_theme.name == 'theme_ptech':
            company_id = http.request.env.company.id
            domain = [('company_id', '=', company_id)]
            service_ids = http.request.env['website.services'].sudo().search(domain)
            partner_ids = http.request.env['website.partners'].sudo().search(domain)
            app_ids = http.request.env['blog.post'].sudo().search([('is_app', '=', True)])

            data = {
                'service_ids': service_ids,
                'partner_ids': partner_ids,
                'app_ids': app_ids,
            }
            print(data)
            return http.request.render('website.homepage', data)
        else:
            return super(WebsitePtech, self).index(**kw)
