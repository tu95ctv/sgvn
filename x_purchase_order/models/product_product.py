# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    po_qty_confirm = fields.Integer("Purchase Order quantity", default=0)
    po_amount_confirm = fields.Float("Purchase Order amount", default=0)
    po_uom_ids = fields.Many2many(
        comodel_name="uom.uom", relation="purchase_uom_product_product_rel",
        column1="product_id", column2="uom_id", string="Purchase Order Unit")
    po_fixed_price = fields.Float("Purchase Fixed price", default=0)