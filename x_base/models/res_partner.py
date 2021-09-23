from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    def read(self, list_fields=None, load='_classic_read'):
        res_model = self._context.get('default_model', False)
        res_id = self._context.get('default_res_id', False)
        if res_model and res_model == 'purchase.order' and 'email' in list_fields:
            po = self.env[res_model].sudo().brose(res_model)
            if po.state in ['draft', 'sent']:
                partner_email_field = 'email_quote_request'
            else:
                partner_email_field = 'email_purchase'
            list_fields += [partner_email_field]
            res = super(ResPartner, self).read(list_fields, load)
            _logger.info('2222222222222222222222 %s', res)

            for r in res:
                r['email'] = r[partner_email_field]
            return res
        return super(ResPartner, self).read(list_fields, load)
