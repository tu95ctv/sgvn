# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _name = 'ss_erp.res.partner.form'
    
    approval_id = fields.Char(compute='_compute_approval', string='Approval ID')
    approval_state = fields.Char('Approval status', compute='_compute_approval')
    res_partner_id = fields.Char('Contact ID', compute='_compute_approval')

