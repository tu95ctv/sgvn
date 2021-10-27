# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_fax_number = fields.Char(
        string="Fax Number", size=20
    )
    organization_id = fields.Many2one(
        'ss_erp.organization', string='Organization')
    x_contact_categ = fields.Many2one(
        'ss_erp.contact.category', string='Contact category', index=True
    )
    x_name_furigana = fields.Char(string="Furigana")
    x_partner_categ = fields.Selection([
        ('customer', 'Customer'),
        ('vendor', 'Supplier'),
        ('multi', 'Customers & Supplier'),
        ('other', 'Other'),
        ], string="Contact classification")
    type = fields.Selection(selection_add=[
        ('for_rfq', 'Address for requesting a quote'),
        ('for_po', 'Order destination'),
        ])
    x_transaction_categ = fields.Many2many('ss_erp.bis.category', 'category_partner_rel', 'categ_id', 'partner_id', string="Transaction classification", index=True)
    x_transaction_department = fields.Many2many('ss_erp.bis.category', 'department_partner_rel', 'department_id', 'partner_id', string="Department", index=True)
    x_is_branch = fields.Boolean(string="Organization in charge", default=True)
    x_branch_name = fields.Many2one('ss_erp.organization', string='Name of organization in charge')
    x_fax = fields.Char('FAX representative')
    x_fax_payment = fields.Char('Fax payment notice')
    x_contract_check = fields.Selection([
        ('contract', '締結'),
        ('no_contract', '締結しない'),
        ('noting', '該当なし'),
        ], string='Transaction basic contract', default='contract', index=True)
    x_contract_memo = fields.Text(string="Reason for fluctuation")
    x_found_year = fields.Char(string='Founding year')
    x_capital = fields.Float(string='Capital')
    x_accounting_period = fields.Char(string='Fiscal year')
    x_revenue = fields.Float(string='Amount of sales')
    x_ordinary_profit = fields.Float(string='Management profit')
    x_license_figure = fields.Char(string='Type of permission')
    x_license_flag_1 = fields.Selection([
        ('minister', '大臣'),
        ('governor', '知事'),
        ('other', 'その他'),
        ], string='Minister / Governor classification', default='minister')
    x_license_flag_2 = fields.Selection([
        ('specific', '特定'),
        ('normal', '一般'),
        ('other', 'その他'),
        ], string='Specific / general classification', default='normal')
    x_license_number = fields.Char(string='Permission number')
    x_license_period = fields.Date(string='Permit date')
    property_product_pricelist = fields.Many2one('product.pricelist', string='Price list')
    x_more_than_amount = fields.Float(string='Amount of 10,000 yen or more')
    x_more_than_deadline = fields.Float(string='Closing date of 10,000 yen or more')
    x_more_than_payment_site = fields.Char(string='Payment site for 10,000 yen or more')
    x_more_than_payment_method = fields.Selection([
        ('cash', '現金'),
        ('check', '小切手'),
        ('transfer', '振込'),
        ('bills', '手形'),
        ('offset', '相殺'),
        ],string='Payment method of 10,000 yen or more', default='transfer')
    x_less_than_amount = fields.Float(string='Amount of less than 10,000 yen')
    x_less_than_deadline = fields.Char(string='Closing date of 10,000 yen or less')
    x_less_than_payment_site = fields.Char('Payment site for 10,000 yen or less')
    less_than_payment_method = fields.Selection([
        ('cash', '現金'),
        ('check', '小切手'),
        ('transfer', '振込'),
        ('bills', '手形'),
        ('offset', '相殺'),
        ],string='Payment method of 10,000 yen or less', default='transfer')
    x_collecting_money = fields.Selection([
        ('yes', '有'),
        ('no', '無'),
    ], string='Collecting money', default='no')
    x_fee_burden = fields.Selection([
        ('other_side', '有'),
        ('our_side', '無'),
    ], string='Fee burden', default='other_side')
    x_bill_site = fields.Char('Bill site', )
    x_purchase_user_id = fields.Many2one('res.users', string='Purchasing person', index=True)
    x_vendor_payment_term = fields.Selection([
        ('ss_rule', '当社規定(規則参照)'),
        ('other', 'その他'),
    ], string='Payment terms and conditions')
    property_supplier_payment_term_id = fields.Many2one('account.payment.term', strint='Payment terms')
    x_other_payment_term = fields.Char(string='Other payment terms')
    x_other_payment_reason = fields.Text(string='Reason for fluctuation')
    x_minimum_cost = fields.Float(string='Minimum purchase price')
    x_payment_terms = fields.Html(related='company_id.x_payment_terms', string='Our regulations on payment terms')
    bank_id = fields.Many2one('res.bank', string='Bank')
    x_bank_branch = fields.Char(string='Branch')
    x_acc_holder_furigana = fields.Char('Furigana')
    x_customer_contract_route = fields.Text(string='Sales motive')
    x_customer_monthly_total_price = fields.Float(string='Monthly sales amount')
    x_vendor_contract_route = fields.Text(string='Purchasing motive')
    x_vendor_material = fields.Text(string='Purchased products')
    x_vendor_monthly_total_price = fields.Float(string='Monthly purchase amount')
    commnet = fields.Text(string='Internal note')


    @api.depends('is_company', 'x_contact_categ')
    def _compute_company_type(self):
        for partner in self:
            if partner.x_contact_categ and partner.x_contact_categ.company_type:
                partner.company_type = partner.x_contact_categ.company_type
            else:
                super(ResPartner, partner)._compute_company_type()

    @api.onchange
    def _onchange_x_contact_categ(self):
        if self.x_contact_categ and self.x_contact_categ.type:
            self.type = self.x_contact_categ.type
