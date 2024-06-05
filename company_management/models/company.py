from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class Company(models.Model):
    _description = 'Companies'
    _name = 'company'

    name = fields.Char(string='Name', required=True)
    employee_idd = fields.One2many('hr.employee', 'company_idd')
    image = fields.Binary(string="Image")
    logo = fields.Binary(string='Logo')
    partner_id = fields.Many2one('hr.employee', string='Contact')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street 2')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')
    currency_id = fields.Many2one('res.currency', string='Currency')
    phone = fields.Char(string='Phone')
    mobile = fields.Char(string='Mobile')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    parent_id = fields.Many2one('company', string='Parent Company')
    sequence = fields.Integer(string='Sequence')
    favicon = fields.Binary(string='Favicon')
    linkedin_profile = fields.Char(string='LinkedIn Profile')
    description = fields.Html(string='Description')
