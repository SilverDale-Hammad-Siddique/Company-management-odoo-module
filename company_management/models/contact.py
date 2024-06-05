from odoo import api, fields, models


class Contacts(models.Model):
    _description = 'Contacts'
    _inherit = 'res.partner'

    # active = fields.Boolean(string="Active", default=True)
    # my_employee = fields.Boolean(string="My Employee", default=True)
    # department_idd = fields.Many2one('department', string="Department")
