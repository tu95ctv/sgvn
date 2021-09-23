# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)

class MailMail(models.Model):
    _inherit = 'mail.mail'

    def _send_prepare_values(self, partner=None):
        _logger.info('333333333333333333 %s', self._context)
        _logger.info('44444444444444444 %s', self.model)

        if self.model == 'purchase.order':
            po = self.env[self.model].sudo().brose(self.res_id)
            if po.state in ['draft', 'sent']:
                partner_email_field = 'email_quote_request'
            else:
                partner_email_field = 'email_purchase'
            if not self._context.get('partner_email_field'):
                return super(MailMail, self).with_context(partner_email_field=partner_email_field)._send_prepare_values(partner)
        return super(MailMail, self)._send_prepare_values(partner)

class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    def send_mail(self, auto_commit=False):
        _logger.info('333333333333333333 MailComposer %s', self._context)
        _logger.info('44444444444444444 MailComposer %s', self)
        return super(MailComposer, self).send_mail(auto_commit=auto_commit)
