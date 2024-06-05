# models.py

from odoo import models, fields


class MyReport(models.Model):
    _name = 'my.report'
    _description = 'My Report'

    name = fields.Char('Name')
    description = fields.Text('Description')
