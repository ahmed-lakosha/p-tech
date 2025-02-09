from odoo import models, fields, api, _


class ThemePtech(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_ptech_post_copy(self, mod):
        self.enable_view('website.template_header_default')
        self.enable_view('website.header_visibility_disappears')
        self.disable_view('website.header_text_element')
        self.disable_view('website.header_search_box')
        self.disable_view('website.header_call_to_action')
        self.enable_view('website.footer_custom')
