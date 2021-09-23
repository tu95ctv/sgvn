from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    def read(self, fields=None, load='_classic_read'):
        _logger.info('1111111111111111111111 %s', self._context)
        _logger.info('2222222222222222222222 %s', fields)
        return super(ResPartner, self).read(fields=fields, load=load)
