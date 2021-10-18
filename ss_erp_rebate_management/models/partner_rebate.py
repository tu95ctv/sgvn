# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import time
from datetime import datetime
import pytz


class PartnerRebate(models.Model):
    _name = 'ss_erp.partner.rebate'
    _description = 'Rebate condition'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _rec_name = 'partner_id'

    name = fields.Char(string='No.', default='New', readonly=1)
    sequence = fields.Integer(string='Sequence', default=10)
    company_id = fields.Many2one(
        "res.company", string="Company",
        default=lambda self: self.env.company.id, index=True
    )
    organization_id = fields.Many2one(
        comodel_name="ss_erp.organization", string="Organization in charge",
        copy=False, index=True,
        help="Organization which create this record."
    )
    responsible_id = fields.Many2one(
        'ss_erp.responsible.department', "Jurisdiction", index=True)
    partner_id = fields.Many2one(
        'res.partner', string='Supplier',
        change_default=True, tracking=True, index=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="You can find a vendor by its Name, TIN, Email or Internal Reference.")
    partner_ref = fields.Char(
        related='partner_id.ref',
        string="Supplier code")
    active = fields.Boolean(
        string="Enable", default=True,
        help="Set active to false to hide the rebate contract without removing it.")
    date_start = fields.Datetime(
        string="Contract start date",
        default=lambda self: fields.Datetime.now().strftime('%Y-%m-%d 00:00:00'))

    date_end = fields.Datetime(
        string="Contract end date",
        default=lambda self: fields.Datetime.now().strftime('%Y-%m-%d 23:59:59'))
    rebate_price = fields.Float("Bounty",)
    rebate_standard = fields.Text("Reward criteria")
    remarks = fields.Text("Memo")
    rebate_goal = fields.Char("The goal")
    rebate_products = fields.Text("Target product")
    currency_id = fields.Many2one(
        'res.currency', default=lambda self: self.env.company.currency_id)
    attachment_number = fields.Integer(
        'Number of Attachments', compute='_compute_attachment_number')

    def _compute_attachment_number(self):
        attachment_data = self.env['ir.attachment'].read_group([
            ('res_model', '=', 'ss_erp.partner.rebate'),
            ('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
        attachment = dict(
            (data['res_id'], data['res_id_count']) for data in attachment_data)
        for record in self:
            record.attachment_number = attachment.get(record.id, 0)

    @api.constrains("date_start", "date_end")
    def _check_dates(self):
        """End date should not be before start date, if not filled

        :raises ValidationError: When constraint is violated
        """
        for record in self:
            if (
                record.date_start
                and record.date_end
                and record.date_start > record.date_end
            ):
                raise ValidationError(
                    _("The starting date cannot be after the ending date.")
                )

    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code(
    #             'ss_erp.partner.rebate') or _('New')
    #     result = super(PartnerRebate, self).create(vals)
    #     return result

    # @api.model
    # def _default_organization_id(self):
    #     return self.env.user.x_organization_id and self.env.user.x_organization_id.id

    def action_get_attachment_view(self):
        self.ensure_one()
        res = self.env['ir.actions.act_window']._for_xml_id(
            'base.action_attachment')
        res['domain'] = [('res_model', '=', 'ss_erp.partner.rebate'),
                         ('res_id', 'in', self.ids)]
        res['context'] = {
            'default_res_model': 'ss_erp.partner.rebate', 'default_res_id': self.id}
        return res

    def action_add_attachment(self):
        action = {
            'name': _("Attachment file"),
            'type': 'ir.actions.act_window',
            'views': [[False, 'form']],
            'target': 'new',
            'context': {
                'default_rebate_id': self.id,
            },
            'res_model': 'partner.rebate.attachment.wizard'
        }
        return action
