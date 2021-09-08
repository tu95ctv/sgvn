# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    email_quote_request = fields.Char("E-mail address for sending a quote request", copy=False)
    email_purchase = fields.Char("Purchase order sending email address", copy=False)
