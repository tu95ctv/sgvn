# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

import logging

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = ['purchase.order', 'x.x_company_organization.org_mixin']

    trans_classify_id = fields.Many2one('x.transaction.classification', "Transaction classification")

    @api.onchange('partner_id')
    def _onchange_partner_id_sgvn(self):
        self.trans_classify_id = self.partner_id.x_transaction_classification and self.partner_id.x_transaction_classification[0].id
        x_organization_id = self.x_organization_id and self.x_organization_id.id
        if self.partner_id and not (self.partner_id.x_organization_id and self.partner_id.x_organization_id.id == x_organization_id):
            return {
                'warning': {
                    'title': _("Alert: Insufficient supplier transaction information"),
                    'message': _("""The purchasing information for [Login User's Organization Name] does not exist for the selected supplier.\nPlease complete the purchase information input / approval of the relevant supplier from the supplier application screen.""")
                },
            }

    @api.onchange('x_organization_id')
    def _onchange_x_organization_id(self):
        x_organization_id = self.x_organization_id and self.x_organization_id.id
        if self.partner_id and not (self.partner_id.x_organization_id and self.partner_id.x_organization_id.id == x_organization_id):
            return {
                'warning': {
                    'title': _("Alert: Insufficient supplier transaction information"),
                    'message': _("""The purchasing information for [Login User's Organization Name] does not exist for the selected supplier.\nPlease complete the purchase information input / approval of the relevant supplier from the supplier application screen.""")
                },
            }

    type = fields.Selection([
        ('normal', 'Usually buy'),
        ('tank_lorry', 'Raleigh delivery'),
    ], string='Purchase type', copy=False, default='normal')
    desired_delivery = fields.Selection([
        ('full', 'Full payment request'),
        ('separated', 'Can be paid in installments'),
    ], string="Desired delivery", copy=False, default='full')
    date_response = fields.Datetime("Response date", copy=False)
    date_issuance = fields.Date("Issuance date", copy=False, default=fields.Date.context_today)
    jurisdiction_id = fields.Many2one('crm.team', "Jurisdiction")
    dest_address_infor = fields.Html("Direct shipping information", copy=False)

    @api.depends('trans_classify_id')
    def _compute_show_construction(self):
        for rec in self:
            construction_trans_id = self.env.ref("sgvn_purchase_quotation.transaction_classification_construction").id
            rec.show_construction = rec.trans_classify_id and rec.trans_classify_id.id == construction_trans_id

    # Displayed only when the transaction classification item of the slip is "Construction"
    show_construction = fields.Boolean("Show Construction", compute='_compute_show_construction')
    construction_name = fields.Char("Construction name")
    construction_site = fields.Char("Construction site")
    construction_period_start = fields.Date('Scheduled construction period', copy=False)
    construction_period_end = fields.Date('Scheduled construction period (end)', copy=False)
    pres_abs_supplies = fields.Selection([
        ('none', 'No'),
        ('having', 'Yes'),
    ], string="Presence/absence of supplies", copy=False, default='none')
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

    # TODO: Hide print with state
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(PurchaseOrder, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                                         submenu=submenu)
        # _logger.info('111111111111111 fields_view_get toolbar print: %s', res.get('toolbar', {}).get('print', []))
        return res

    # Update file attachment for mail template with trans_classify_id
    def action_rfq_send(self):
        res = super(PurchaseOrder, self).action_rfq_send()
        if self.trans_classify_id:
            if self.trans_classify_id.id == self.env.ref("sgvn_purchase_quotation.transaction_classification_construction").id:
                res['context'].update({
                    'default_template_id': self.env.ref("sgvn_purchase_quotation.report_purchasequotation").id
                })
            elif self.trans_classify_id.id == self.env.ref("x_partner.transaction_classification_gas_equipment").id:
                res['context'].update({
                    'default_template_id': self.env.ref("sgvn_purchase_quotation.report_estimate_request").id
                })
        return res


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    delivery_destination_id = fields.Many2one('stock.location', "Delivery destination")

    @api.model
    def default_get(self, fields):
        rec = super(PurchaseOrderLine, self).default_get(fields)
        params = self._context.get('params')
        if params and params.get('id'):
            order_id = self.env['purchase.order'].browse(params.get('id'))
            rec['delivery_destination_id'] = order_id.x_organization_id.x_purchase_stock_location_id.id if order_id.x_organization_id and order_id.x_organization_id.x_purchase_stock_location_id else False
        else:
            x_organization_id = self.env.user.x_organization_id
            rec['delivery_destination_id'] = x_organization_id.x_purchase_stock_location_id.id if x_organization_id and x_organization_id.x_purchase_stock_location_id else False
        return rec

    # @api.onchange('order_id', 'order_id.x_organization_id')
    # def _onchange_partner_id_sgvn(self):
    #     self.delivery_destination_id = self.order_id.x_organization_id.x_purchase_stock_location_id.id if self.order_id.x_organization_id.x_purchase_stock_location_id else False
