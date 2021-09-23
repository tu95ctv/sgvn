# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger(__name__)

class MailMail(models.Model):
    _inherit = 'mail.mail'

    # def _send_prepare_values(self, partner=None):
    #     # if self.model == 'purchase.order':
    #     #     po = self.env[self.model].sudo().brose(self.res_id)
    #     #     if po.state in ['draft', 'sent']:
    #     #         partner_email_field = 'email_quote_request'
    #     #     else:
    #     #         partner_email_field = 'email_purchase'
    #     #     if not self._context.get('partner_email_field'):
    #     #         return super(MailMail, self).with_context(partner_email_field=partner_email_field)._send_prepare_values(partner)
    #     _logger.info('22222222222222222222  _send_prepare_values%s', self._context)

    #     res = super(MailMail, self)._send_prepare_values(partner)
    #     _logger.info('44444444444444444444  _send_prepare_values %s', res)

    #     return res

    def _send_prepare_values(self, partner=None):
        """Return a dictionary for specific email values, depending on a
        partner, or generic to the whole recipients given by mail.email_to.

            :param Model partner: specific recipient partner
        """
        self.ensure_one()
        body = self._send_prepare_body()
        body_alternative = tools.html2plaintext(body)
        if partner:
            email_to = [tools.formataddr((partner.name or 'False', partner.email or 'False'))]
            _logger.info('777777775555555555555555  _send_prepare_values %s', partner.email)
            _logger.info('77777777777777777  _send_prepare_values %s', email_to)
        else:
            email_to = tools.email_split_and_format(self.email_to)
            _logger.info('88888888888888888  _send_prepare_values %s', email_to)
        res = {
            'body': body,
            'body_alternative': body_alternative,
            'email_to': email_to,
        }
        return res
