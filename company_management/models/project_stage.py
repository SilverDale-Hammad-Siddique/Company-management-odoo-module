from odoo import models, fields


class Stage(models.Model):
    _name = 'my.project.stage'  # Ensure the _name follows this format
    _description = 'Stage'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)

