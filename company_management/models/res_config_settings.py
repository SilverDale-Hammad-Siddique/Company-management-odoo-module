# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = ['res.config.settings']

    geo_location = fields.Char(string='Geolocation')
