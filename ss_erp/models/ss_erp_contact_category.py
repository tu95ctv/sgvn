# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ContactCategory(models.Model):
    _name = 'ss_erp.contact.category'
    _description = 'Contact Category'

    name = fields.Char(string='Name')
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)
    company_type = fields.Selection(
        [('person', 'Person'), ('company', 'Company')], string='Company type')
    type = fields.Selection([
        ('contact', 'Contacts'),
        ('invoice', 'Invoice'),
        ('delivery', 'Delivery to'),
        ('for_rfq', 'Address for requesting a quote'),
        ('for_po', 'Order destination'),
        ('other', 'Other addresses'),
        ('private', 'Personal address'),
    ], string='Address type')
    description = fields.Char(string='explanation')
    basic = fields.Char('Basic')
    has_partner_info = fields.Boolean(
        string="Account Overview tab", default=True)
    has_parent = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='related company', default='required')
    has_ref = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Customer code', default='required')
    has_address = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Business address', default='required')
    has_function = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Job title', default='required')
    has_phone = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='TEL representative', default='required')
    has_mobile = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='TEL direct', default='required')
    has_x_fax = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='FAX representative', default='required')
    has_x_fax_payment = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Fax payment notice', default='required')
    has_x_contract_check = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Transaction basic contract', default='required')
    has_email = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Email', default='required')
    has_website = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Website link', default='required')
    has_vat = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Tax ID', default='required')
    has_title = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Title', default='required')
    has_category = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Tag', default='required')
    has_x_found_year = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Founding year', default='required')
    has_x_capital = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Capital', default='required')
    has_performance_info = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Achievement information', default='required')
    has_construction_info = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Construction permit', default='required')
    has_user = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Sales person', default='required')
    has_property_delivery_carrier = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Shipping method', default='required')
    has_team = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Sales team', default='required')
    has_property_payment_term = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Payment terms', default='required')
    has_property_product_pricelist = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Price list', default='required')
    has_sales_term = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Transaction terms', default='required')
    has_x_collecting_money = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Collecting money', default='required')
    has_x_fee_burden = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Fee burden', default='required')
    has_x_bill_site = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Bill site', default='required')
    has_x_purchase_user = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Purchasing person', default='required')
    has_x_vendor_payment_term = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Payment terms and conditions', default='required')
    has_property_supplier_payment_term = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Payment terms', default='required')
    has_x_minimum_cost = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Minimum purchase price', default='required')
    has_x_payment_terms = fields.Boolean(
        string='Our regulations on payment terms', default=True)
    has_property_account_position = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Accounting position', default='required')
    has_bank_accounts = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Bank accounts', default='required')
    has_sales_note = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Sales related', default='required')
    has_purchase_note = fields.Selection([
        ('required', 'Required'),
        ('optional', 'Optional'),
        ('no', 'No'),
    ], string='Purchasing related', default='required')
