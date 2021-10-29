# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartnerForm(models.Model):
    _inherit = ['res.partner']
    _name = 'ss_erp.res.partner.form'
    _description = 'Res Partner Form'

    channel_ids = fields.Many2many(
        'mail.channel', 'mail_channel_profile_partner_form', 'partner_id', 'channel_id', copy=False)
    meeting_ids = fields.Many2many('calendar.event', 'calendar_event_res_partner_form_rel',
                                   'res_partner_id', 'calendar_event_id', string='Meetings', copy=False)
    x_transaction_categ = fields.Many2many('ss_erp.bis.category', 'category_partner_form_rel',
                                           'categ_id', 'partner_id', string="Transaction classification", index=True)
    x_transaction_department = fields.Many2many(
        'ss_erp.bis.category', 'department_partner_form_rel', 'department_id', 'partner_id', string="Department", index=True)
    approval_id = fields.Char(string='Approval ID')
    approval_state = fields.Char('Approval status')
    res_partner_id = fields.Char('Contact ID')

# compute='_compute_approval',
