# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    saldo_vencido = fields.Float(string='Saldo Vencido', readonly=True, copy=False)
    objetivo = fields.Text(string='Objetivo')
