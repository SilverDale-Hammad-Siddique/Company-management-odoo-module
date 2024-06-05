from odoo import api, fields, models


class Activity(models.Model):
    _name = 'activity'
    _description = 'Activity'

    name = fields.Char(string='Name')
