from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BlogPost(models.Model):
    _inherit = 'blog.post'
    _order = "sequence, id"

    is_app = fields.Boolean(string="Is Odoo App")
    icon = fields.Binary(string="Icon", store=True)
    sequence = fields.Integer('Sequence', default=10)

    @api.constrains('icon', 'is_app')
    def _check_type_and_fakeness(self):
        for record in self:
            if record.is_app and not record.icon:
                raise ValidationError(
                    "this Blog post is odoo app and must set the icon field."
                )
