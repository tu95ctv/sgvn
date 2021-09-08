from odoo import fields, models


class PartnerPerformance(models.Model):
    _name = "x.partner.sales.information"
    _description = "Partner Performance"

    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Contact", domain="[('company_type', '=', 'company')]",
        readonly=True, copy=False, ondelete="cascade"
    )
    currency_id = fields.Many2one(
        comodel_name="res.currency", string="Currency",
        related="partner_id.currency_id", store=True, ondelete="cascade"
    )
    x_fiscal_year = fields.Char(string="Fiscal Year", default=str(fields.Date.today().year))
    x_ammount_of_sale = fields.Monetary(string="Ammount Of Sales", currency_field="currency_id")
    x_management_profit = fields.Monetary(string="Management Profit", currency_field="currency_id")
