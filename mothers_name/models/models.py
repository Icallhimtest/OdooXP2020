# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mothers_name(models.Model):
    _inherit = 'res.partner'

    mothers_name = fields.Char()
