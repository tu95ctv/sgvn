# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class MultiApprovers(models.Model):
    _name = 'ss_erp.multi.approvers'
    _description = 'Multi Approvers'

    name = fields.Char(string='Name')
    active = fields.Boolean('Active', default=True)
    x_approval_seq = fields.Integer('Seq.', default=10)
    x_request_id = fields.Many2one('approval.request', string='Request')
    x_company_id = fields.Many2one(
        'res.company', related='x_request_id.company_id', store=True, copy=False, index=True)
    x_existing_request_user_ids = fields.Many2many(
        'res.users', 'existing_request_users_approvers_rel', 'user_id', 'approver_id', string='Existing Request User', readonly=True)
    x_approver_group_ids = fields.Many2many(
        'res.users', 'approver_group_users_approvers_rel', 'user_id', 'approver_id', string='Approver group', store=True, copy=True)
    x_related_user_ids = fields.Many2many(
        'res.users', 'related_users_approvers_rel', 'user_id', 'approver_id', string='Stakeholder group', store=True, copy=True)
    x_is_manager_approver = fields.Boolean(
        string='Manager approval', store=True, copy=True, default=False)
    x_user_status = fields.Selection([
        ('new', 'New'),
        ('pending', 'Unapproved'),
        ('approved', 'Approved'),
        ('refused', 'Rejected'),
        ('cancel', 'Cancel'),
    ], string='status', default='new', store=True, copy=True)
    x_minimum_approvers = fields.Integer('Minimum number of approved people')
