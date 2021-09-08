# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    notes_construction_contract = fields.Html("Notes on construction contract", copy=False)
    estimated_subcontracting_work = fields.Html("Estimated price and estimated period for subcontracting work", copy=False)
