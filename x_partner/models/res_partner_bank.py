from odoo import fields, models


class ResPartnerBank(models.Model):
    _name = "res.partner.bank"
    _inherit = ["res.partner.bank", "x.x_company_organization.org_mixin"]

    x_deposit_type = field_name = fields.Selection([
        ('usually', 'Usually'), ('current', 'Current')
    ], string='Deposit Type')
    x_furigana = field_name = fields.Char(string='Furigana')
