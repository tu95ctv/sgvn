# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class OrganizationCategory(models.Model):
    _name = 'ss_erp.organization.category'
    _description = 'Organization'


    name = fields.Char(string='Category name')
    company_id = fields.Many2one(
        'res.company', string='Company',required=True,
        readonly=True, default=lambda self: self.env.company)
    sequence = fields.Integer("Sequence")
    active = fields.Boolean(default=True, help="If the active field is set to False, it will allow you to hide the payment terms without removing it.")
    hierarchy_number = fields.Integer("Hierarchy")
