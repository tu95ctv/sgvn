# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.translate import html_translate

import logging

_logger = logging.getLogger(__name__)

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    x_bis_categ_id = fields.Many2one('ss_erp.bis.category', string="Transaction classification", copy=True, index=True)
    x_po_type = fields.Selection([
        ('normal', 'Normal purchase'),
        ('industry_lorry', 'Raleigh delivery(industrial gas)'),
        ('lp_lorry', 'Raleigh delivery(LP gas)'),
        ('lng_lorry', 'Raleigh delivery(LNG gas)'),
        ('dropship', 'Direct delivery'),
    ], string="Purchase type", default='normal', index=True, copy=False)

    x_rfq_issue_date = fields.Date("Quotation request date")
    x_po_issue_date = fields.Date("Order sending date")
    x_desired_delivery = fields.Selection([
        ('full', 'Hope for full payment'),
        ('separated', 'Can be paid in installments'),
    ], string="Desired delivery", default='full', copy=True)
    x_dest_address_info = fields.Html("Direct shipping information")
    x_truck_number = fields.Char("Car number")
    x_organization_id = fields.Many2one('ss_erp.organization', string="Organization in charge", index=True)
    x_responsible_dept_id = fields.Many2one('ss_erp.responsible.department', string="Jurisdiction", index=True)
    x_mkt_user_id = fields.Many2one('res.users', string="Sales representative", index=True, default=lambda self: self.env.user)

    # Construction information
    @api.depends('x_bis_categ_id')
    def _compute_show_construction(self):
        rec_construction_id = self.env.ref("ss_erp_master.ss_erp_bis_category_data_0").id
        for rec in self:
            rec.x_is_construction = True if self.x_bis_categ_id and self.x_bis_categ_id.id == rec_construction_id else False

    x_is_construction = fields.Boolean("Is construction?", compute='_compute_show_construction', compute_sudo=True)
    x_construction_name = fields.Char("Construction name")
    x_construction_sopt = fields.Char("construction site")
    x_construction_period_start = fields.Date("Scheduled construction period start")
    x_construction_period_end = fields.Char("Scheduled construction period ends")
    x_supplies_check = fields.Selection([
        ('no', 'None'),
        ('exist', 'Can be'),
    ], string="Presence or absence of supplies", default='no')
    x_supplies_info = fields.Char("Supplies")
    x_construction_payment_term = fields.Char("Payment terms", readonly=True, default=_("Construction payment conditions (deadline at the end of the month and payment at the end of the following month according to our regulations)"))

    x_explanation_check = fields.Selection([
        ('no', 'None'),
        ('exist', 'Can be'),
    ], string="Presence or absence of the current theory", default='no')
    x_explanation_date = fields.Date("Current date")
    x_explanation_spot = fields.Char("Current theory place")
    x_construction_other = fields.Text("others")
    x_construction_payment_cash = fields.Float("Cash")
    x_construction_payment_bill = fields.Float("Bills")
    x_construction_contract_notice = fields.Html("Notes on construction contract", copy=True, default=lambda self: self.env.user.company_id.x_construction_contract_notice)
    x_construction_subcontract = fields.Html("Estimated price and estimated period for subcontracting work", copy=True, default=lambda self: self.env.user.company_id.x_construction_subcontract)
