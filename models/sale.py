# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    venta_credito = fields.Boolean(string='Venta a Crédito', readonly=True, copy=False)
    preventa = fields.Boolean(string='Preventa', readonly=True, copy=False)
