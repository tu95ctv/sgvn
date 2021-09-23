# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    email_quote_request = fields.Char("E-mail address for sending a quote request", copy=False)
    email_purchase = fields.Char("Purchase order sending email address", copy=False)

    def read(self, list_fields=None, load='_classic_read'):
        _logger.info('22222222222222222222 %s', self._context)

        # res_model = self._context.get('default_model', False)
        # res_id = self._context.get('default_res_id', False)
        # if res_model and res_id and res_model == 'purchase.order' and 'email' in list_fields:
        #     if 'mail_post_autofollow' in self._context or 'force_email' in self._context or 'show_email' in self._context:
        #         po = self.env[res_model].sudo().browse(res_id)
        #         if po.state in ['draft', 'sent']:
        #             partner_email_field = 'email_quote_request'
        #         else:
        #             partner_email_field = 'email_purchase'
        #         list_fields += [partner_email_field]
        #         res = super(ResPartner, self).read(list_fields, load)
        #         for r in res:
        #             r['email'] = r[partner_email_field]
        #         _logger.info('2222222222222222222222 %s', res)
        #         return res
        # res = super(ResPartner, self).read(list_fields, load)
        # _logger.info('555555555555555555555555 %s', res)
        if 'partner_email_field' in self._context:
            list_fields += [self._context.get('partner_email_field')]
            res = super(ResPartner, self).read(list_fields, load)
            for r in res:
                r['email'] = r[partner_email_field]
            _logger.info('33333333333333333 %s', res)

            return res
        res = super(ResPartner, self).read(list_fields, load)
        _logger.info('44444444444444444444 %s', res)
        return res
