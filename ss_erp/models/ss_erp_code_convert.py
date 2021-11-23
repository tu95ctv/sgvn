# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CodeConvert(models.Model):
    _name = 'ss_erp.code.convert'
    _description = 'Code Convert'

    external_system = fields.Many2one('ss_erp.external.system.type', string='External system', required=True)
    convert_code_type = fields.Many2one('ss_erp.convert.code.type', string='Conversion code type', required=True)
    external_code = fields.Char(string='Customer code (external)')
    internal_code = fields.Char(string='Customer code (Odoo)')
    priority_conversion = fields.Boolean(string='Priority conversion destination', required=True, default=False)