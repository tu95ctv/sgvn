# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResPartnerForm(models.Model):
    _inherit = 'res.partner'
    _name = 'ss_erp.res.partner.form'
    _description = 'Res Partner Form'

    approval_id = fields.Char(string="Approval ID")
    approval_state = fields.Char(string='Approval status')
    res_partner_id = fields.Char(string='Contact ID')

    # Override fields and fucntion in res.partner
    channel_ids = fields.Many2many(
        'mail.channel', 'mail_channel_profile_partner_form', 'partner_id', 'channel_id', copy=False)
    meeting_ids = fields.Many2many('calendar.event', 'calendar_event_res_partner_form_rel',
        'res_partner_id', 'calendar_event_id', string='Meetings', copy=False)
    x_transaction_categ = fields.Many2many('ss_erp.bis.category', 'category_partner_form_rel',
        'categ_id', 'partner_id', string="Transaction classification", index=True)
    x_transaction_department = fields.Many2many(
        'ss_erp.bis.category', 'department_partner_form_rel', 'department_id', 'partner_id', string="Department", index=True)

    property_account_payable_id = fields.Many2one('account.account', string="Account Payable",
        domain="[('internal_type', '=', 'payable'), ('deprecated', '=', False), ('company_id', '=', current_company_id)]",
        help="This account will be used instead of the default one as the payable account for the current partner",
        required=False)
    property_account_receivable_id = fields.Many2one('account.account', company_dependent=True,
        string="Account Receivable",
        domain="[('internal_type', '=', 'receivable'), ('deprecated', '=', False), ('company_id', '=', current_company_id)]",
        help="This account will be used instead of the default one as the receivable account for the current partner",
        required=False)

    @api.depends('is_company', 'parent_id.commercial_partner_id')
    def _compute_commercial_partner(self):
        for partner in self:
            partner.commercial_partner_id = False

    @api.depends('user_ids.share', 'user_ids.active')
    def _compute_partner_share(self):
        for partner in self:
            partner.partner_share = False

    @api.depends('purchase_line_ids')
    def _compute_on_time_rate(self):
        for partner in self:
            partner.on_time_rate = -1

    def _message_add_suggested_recipient(self, result, partner=None, email=None, reason=''):
        return result

    def name_get(self):
        results = []
        for rec in self:
            results.append((rec.id, rec.name))
        return results

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if name:
            recs = self.search([('ref', 'ilike', name)] + args, limit=limit)
        if not recs:
            recs = self.search([('name', operator, name)] + args, limit=limit)
        return recs.name_get()

    def write(self, values):
        res = super(ResPartnerForm, self).write(values)
        if 'approval_state' in values and values.get('approval_state') == 'approved':
            self._action_process()

    def _action_process(self):
        DEFAULT_FIELDS = ['id', 'create_uid', 'create_date', 'write_uid', 'write_date',
                '__last_update', 'approval_id', 'approval_state', 'meeting_ids']
        for form_id in self:
            vals = {}
            for name, field in form_id._fields.items():
                if name not in DEFAULT_FIELDS \
                        and form_id._fields[name].type not in ['one2many'] \
                        and not form_id._fields[name].compute:
                    if form_id._fields[name].type == 'many2many':
                        value = getattr(form_id, name, ())
                        value = [(5, 0)] + [(6, 0, value.ids)] if value else False
                    else:
                        value = getattr(form_id, name)
                        if form_id._fields[name].type == 'many2one':
                            value = value.id if value else False

                    vals.update({name: value})
            res_partner_id = vals.pop('res_partner_id')
            if not res_partner_id:
                # Create partner with contact form
                partner_id = self.env['res.partner'].create(vals)
                form_id.write({'res_partner_id': partner_id.id})
            else:
                # Update partner with contact form
                partner_id = self.env['res.partner'].browse(int(res_partner_id))
                partner_id.write(vals)
