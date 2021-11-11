# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class ApprocalRejectWizard(models.TransientModel):
    _name = 'approval.request.reject.wizard'
    _description = 'Approval Reject Wizard'

    request_id = fields.Many2one('approval.request', 'Approval Request')
    reason_reject = fields.Char('Reason for rejection')

    def action_confirm(self):
        self.request_id.sudo().write({'x_reject': self.reason_reject})
        self.request_id.action_refuse()
        return True
