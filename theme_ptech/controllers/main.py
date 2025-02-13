from odoo import http, models, fields
from odoo.addons.website.controllers.main import Website
from odoo.http import request


class WebsitePtech(Website):
    def index(self, **kw):
        current_website = http.request.website
        active_theme = current_website.theme_id

        if active_theme and active_theme.name == 'theme_ptech':
            company_id = http.request.env.company.id
            domain = [('company_id', '=', company_id)]
            service_ids = http.request.env['website.services'].sudo().search(domain)
            data = {
                'service_ids': service_ids,
            }
            return http.request.render('website.homepage', data)
        else:
            return super(WebsitePtech, self).index(**kw)
