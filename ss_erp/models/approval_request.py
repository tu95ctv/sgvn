# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    x_department_id = fields.Many2one(
        'hr.employee', string='Application department')
    x_organization_id = fields.Many2one(
        'ss_erp.organization', string='Application organization')
    x_contact_form_id = fields.Many2one(
        'ss_erp.res.partner.form', string='Contact application form')
    x_inventory_order_ids = fields.Many2many(
        'stock.inventory', 'inventory_request_rel', 'inventory_id', 'request_id', string='Inventory slip')
    x_sale_order_ids = fields.Many2many(
        'sale.order', 'sale_order_request_rel', 'sale_id', 'request_id', string='Quotation slip')
    x_account_move_ids = fields.Many2many(
        'account.move', 'account_move_request_rel', 'move_id', 'request_id', string='Purchase request slip')
    x_purchase_order_ids = fields.Many2many(
        'purchase.order', 'purchase_request_rel', 'purchase_id', 'request_id', string='Quotation request slip')
    x_payment_date = fields.Date('Invoice closing date')
    x_purchase_material = fields.Text('Purchased products')
    x_cash_amount = fields.Float('Cash purchase amount')
    x_cash_payment_date = fields.Date('Cash payment date')
    x_prepay_amount = fields.Float('Prepaid purchase amount')
    x_prepay_payment_date = fields.Date('Prepaid payment date')
    x_payment_reason = fields.Text('Reason for payment')
    x_transfer_preferred_date = fields.Date('Desired remittance date')
    x_present_date = fields.Date('Balance current date')
    x_cash_balance = fields.Float('Cash balance')
    x_bank_balance = fields.Float('Deposit balance')
    x_transfer_date = fields.Date('Remittance date')
    multi_approvers_ids = fields.One2many(
        'ss_erp.multi.approvers', 'x_request_id', string='Multi-step approval')
    # FIELD RELATED
    has_x_organization = fields.Selection(
        related='category_id.has_x_organization', store=True)
    has_x_department = fields.Selection(
        related='category_id.has_x_department', store=True)
    has_x_reject = fields.Selection(
        related='category_id.has_x_reject', store=True)
    has_x_contact_form_id = fields.Selection(
        related='category_id.has_x_contact_form_id', store=True)
    has_x_inventory_order_ids = fields.Selection(
        related='category_id.has_x_inventory_order_ids', store=True)
    has_x_sale_order_ids = fields.Selection(
        related='category_id.has_x_sale_order_ids', store=True)
    has_x_account_move_ids = fields.Selection(
        related='category_id.has_x_account_move_ids', store=True)
    has_x_payment_date = fields.Selection(
        related='category_id.has_x_payment_date', store=True)
    has_x_purchase_material = fields.Selection(
        related='category_id.has_x_purchase_material', store=True)
    has_x_cash_amount = fields.Selection(
        related='category_id.has_x_cash_amount', store=True)
    has_x_cash_payment_date = fields.Selection(
        related='category_id.has_x_cash_payment_date', store=True)
    has_x_prepay_amount = fields.Selection(
        related='category_id.has_x_prepay_amount', store=True)
    has_x_prepay_payment_date = fields.Selection(
        related='category_id.has_x_prepay_payment_date', store=True)
    has_x_payment_reason = fields.Selection(
        related='category_id.has_x_payment_reason', store=True)
    has_x_purchase_order_ids = fields.Selection(
        related='category_id.has_x_purchase_order_ids', store=True)
    has_x_transfer_preferred_date = fields.Selection(
        related='category_id.has_x_transfer_preferred_date', store=True)
    has_x_present_date = fields.Selection(
        related='category_id.has_x_present_date', store=True)
    has_x_cash_balance = fields.Selection(
        related='category_id.has_x_cash_balance', store=True)
    has_x_bank_balance = fields.Selection(
        related='category_id.has_x_bank_balance', store=True)
    has_x_transfer_date = fields.Selection(
        related='category_id.has_x_transfer_date', store=True)
    
