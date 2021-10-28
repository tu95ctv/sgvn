# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons.approvals.models.approval_category import CATEGORY_SELECTION


class ApprovalCategory(models.Model):
    _inherit = 'approval.category'

    has_x_organization = fields.Selection(
        CATEGORY_SELECTION, string="Application organization", default="no",)
    has_x_department = fields.Selection(
        CATEGORY_SELECTION, string="Application department", default="no",)
    has_x_reject = fields.Selection(
        CATEGORY_SELECTION, string="Reason for rejection", default="no",)
    has_x_contact_form = fields.Selection(
        CATEGORY_SELECTION, string="Contact application form", default="no",)
    has_x_inventory_order_id = fields.Selection(
        CATEGORY_SELECTION, string="Inventory slip", default="no",)
    has_x_sale_order_id = fields.Selection(
        CATEGORY_SELECTION, string="Quotation slip", default="no",)
    has_x_account_move_id = fields.Selection(
        CATEGORY_SELECTION, string="Purchase request slip", default="no",)
    x_is_multiple_approval = fields.Boolean(string='Multi-step approval', default=False)
    multiple_approval_ids = fields.Many2one