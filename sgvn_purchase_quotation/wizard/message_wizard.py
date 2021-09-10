from odoo import api, fields, models

class PurchaseMsgWizard(models.TransientModel):
    _name = 'purchase.message.wizard'
    _description = 'Purchase message wizard'

    message = fields.Text(string="Message", readonly=True, store=True)
