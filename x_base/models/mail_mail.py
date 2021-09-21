# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class MailMail(models.Model):
    _inherit = 'mail.mail'

    def _send_prepare_values(self, partner=None):
        if self.model == 'purchase.order':
            po = self.env[self.model].sudo().brose(self.res_id)
            if po.state in ['draft', 'sent']:
                partner_email_field_name = 'email_quote_request'
            else:
                partner_email_field_name = 'email_purchase'
            if not self._context.get('partner_email_field'):
                return super(MailMail, self).with_context(partner_email_field_name=partner_email_field_name)._send_prepare_values(partner)
        return super(MailMail, self)._send_prepare_values(partner)
