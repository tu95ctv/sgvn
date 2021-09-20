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
        self.fixed_price = self.product_id and self.product_id.po_fixed_price

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    date_issuance_order = fields.Date("Purchase order issuance date", copy=False)

    def button_confirm(self):
        res = super(PurchaseOrder, self).button_confirm()
        for order in self:
            order.write({'date_issuance_order': fields.Date.context_today(self)})
        return res

    def _check_unit_line_product(self, line):
        if line.product_id.po_uom_ids and line.product_uom in line.product_id.po_uom_ids:
            return True
        return False

    def _check_qty_line_product(self, line):
        line_qty = line.product_uom_qty
        if line.product_id.po_qty_confirm and line_qty <= line.product_id.po_qty_confirm:
            return True
        return False

    def _check_amount_line_product(self, line):
        line_amount = line.price_subtotal
        if line.product_id.po_amount_confirm and line_amount <= line.product_id.po_amount_confirm:
            return True
        return False

    def action_button_confirm(self):
        msg = ""
        for order in self:
            for line in order.order_line:
                if not self._check_amount_line_product(line):
                    msg = _("The subtotal of the purchase order item exceeds the standard value.\n\nDo you want to place an order as it is?")
                    break
                if not self._check_qty_line_product(line):
                    msg = _("The quantity of the purchase order item exceeds the standard value.\n\nDo you want to place an order as it is?")
                    break
                if not self._check_unit_line_product(line):
                    msg = _("The unit of the purchase order item is a unit other than the set value.\n\nDo you want to place an order as it is?")
                    break
        if msg:
            action = {
                'name': _("Purchase order slip: Confirmed"),
                'type': 'ir.actions.act_window',
                'views': [[False, 'form']],
                'target': 'new',
                'context': {
                    'default_po_id': self.id,
                    'default_msg': msg,
                    'default_type': 'confirm',
                },
                'res_model': 'purchase.order.confirm.wizard'
            }
            return action
        return self.button_confirm()

    def action_button_cancel(self):
        msg = _("Do you want to cancel an order?")

        action = {
            'name': _("Purchase order slip: Cancel"),
            'type': 'ir.actions.act_window',
            'views': [[False, 'form']],
            'target': 'new',
            'context': {
                'default_po_id': self.id,
                'default_msg': msg,
                'default_type': 'cancel',
            },
            'res_model': 'purchase.order.confirm.wizard'
        }
        return action

    def button_cancel(self):
        for order in self:
            for inv in order.invoice_ids:
                if inv and inv.state not in ('cancel', 'draft'):
                    raise UserError(_("Unable to cancel this purchase order. You must first cancel the related vendor bills."))

        self.write({'state': 'cancel'})
