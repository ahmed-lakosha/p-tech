from odoo import models, fields


class WebsiteServices(models.Model):
    _name = "website.services"
    _order = "sequence, id"

    title = fields.Char('Title', required=True, translate=True)
    image = fields.Binary(string='Image', store=True)
    description = fields.Text('Description', required=True, translate=True)
    company_id = fields.Many2one('res.company', string='Company', change_default=True,
                                 default=lambda self: self.env.company)
    sequence = fields.Integer('Sequence', default=10)
