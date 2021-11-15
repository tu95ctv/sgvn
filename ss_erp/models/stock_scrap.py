# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    organization_id = fields.Many2one(
        'ss_erp.organization', string='Organization name')
    responsible_dept_id = fields.Many2one(
        'ss_erp.responsible.department', string='Jurisdiction')
    scrap_type = fields.Selection([
        ('retained', 'Disposal of long-term retained products'),
        ('expired', 'Disposal of expired products'),
        ('damaged', 'Disposal of damaged products'),
        ('ingredient_defect', 'Disposal of defective products(NG)'),
        ('damage_compensation', 'Damage compensation due to accident during shipping'),
        ('products_scrap', 'Disposal of products in process / manufactured products'),
    ], string='Disposal type')
