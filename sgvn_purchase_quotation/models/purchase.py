# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = ['purchase.order', 'x.x_company_organization.org_mixin']

    trans_classify_id = fields.Many2one('x.transaction.classification', "Transaction classification")

    @api.onchange("partner_id")
    def _onchange_partner_id_trans(self):
        self.trans_classify_id = self.partner_id.x_transaction_classification[0].id if self.partner_id.x_transaction_classification else False

    type = fields.Selection([
        ('normal', 'Usually buy'),
        ('tank_lorry', 'Raleigh delivery'),
    ], string='Purchase type', copy=False, default='normal')
    desired_delivery = fields.Selection([
        ('full', 'Full payment request'),
        ('separated', 'Can be paid in installments'),
    ], string='Desired delivery', copy=False, default='full')
    date_response = fields.Datetime("Response date", copy=False)
    date_issuance = fields.Date("Issuance date", copy=False, default=fields.Date.context_today)
    jurisdiction_id = fields.Many2one('crm.team', "Jurisdiction")
    dest_address_infor = fields.Html("Direct shipping information", copy=False)

    # Displayed only when the transaction classification item of the slip is "Construction"
    construction_name = fields.Char("Construction name")
    construction_site = fields.Char("Construction site")
    construction_period_start = fields.Date('Scheduled construction period', copy=False)
    construction_period_end = fields.Date('Scheduled construction period (end)', copy=False)
    pres_abs_supplies = fields.Selection([
        ('none', 'No'),
        ('having', 'Yes'),
    ], string='Presence/absence of supplies', copy=False, default='none')
    construction_supplies = fields.Char("Supplies")
    construction_payment_term = fields.Char("Payment terms", readonly=True, default=_("Dealine at the end of the month, payment at the end of the following month according to our regulations"))
    construction_cash = fields.Float("Cash")
    construction_bills = fields.Float("Bills")
    pres_abs_current_theory = fields.Selection([
        ('none', 'No'),
        ('explanation', 'Yes'),
    ], string='Presence/absence of the current theory', copy=False, default='none')
    construction_current_date = fields.Date('Current date', copy=False)
    construction_current_place = fields.Char('Current theory place', copy=False)
    construction_others = fields.Text('others', copy=False)
    notes_construction_contract = fields.Html("Notes on construction contract", related="company_id.notes_construction_contract")
    estimated_subcontracting_work = fields.Html("Estimated price and estimated period for subcontracting work", related="company_id.estimated_subcontracting_work")

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    # The initial value reflects the delivery destination of the organization in charge of the slip
    delivery_destination_id = fields.Many2one('stock.location', "Delivery destination")
