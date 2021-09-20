# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    fixed_price = fields.Float("Fixed price")

    @api.onchange('product_id')
    def _onchange_product_id_sgvn(self):
        self.fixed_price = self.product_id and self.product_id.fixed_price

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    date_issuance_order = fields.Date("Purchase order issuance date", copy=False)
