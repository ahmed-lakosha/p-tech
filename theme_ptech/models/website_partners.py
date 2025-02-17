from odoo import models, fields


class WebsitePartners(models.Model):
    _name = "website.partners"
    _order = "sequence, id"

    name = fields.Char('Name', required=True, translate=True, requered=True)
    image = fields.Binary(string='Image', store=True, requered=True)
    company_id = fields.Many2one('res.company', string='Company', change_default=True,
                                 default=lambda self: self.env.company)
    sequence = fields.Integer('Sequence', default=10)
