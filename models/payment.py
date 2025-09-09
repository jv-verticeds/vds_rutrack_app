# -*- coding: utf-8 -*-

from odoo import fields, models

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    pago_app = fields.Boolean(string='Pago desde App', readonly=True, copy=False)
