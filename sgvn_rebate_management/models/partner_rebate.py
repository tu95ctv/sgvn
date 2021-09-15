# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class PartnerRebate(models.Model):
    _name = 'x.partner.rebate'
    _description = 'Rebate condition'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    def _default_employee(self):
        return self.env.user.employee_id

    name = fields.Char(string='No.', default='New', readonly=1)
    sequence = fields.Integer(string='Sequence', default=10)
    state = fields.Selection([('on_going', 'On going'), ('expired', 'Expired'), ('closed', 'Closed')], string='Status', default='on_going')
    company_id = fields.Many2one(
        "res.company", string="Company", required=True,
        default=lambda self: self.env.company.id
    )
    x_organization_id = fields.Many2one(
        comodel_name="x.x_company_organization.res_org", string="Organization",
        copy=False, default=lambda self: self._default_organization_id(),
        help="Organization which create this record."
    )
    jurisdiction_id = fields.Many2one('crm.team', "Jurisdiction")
    partner_id = fields.Many2one('res.partner', string='Supplier', required=True, change_default=True, tracking=True, domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]", help="You can find a vendor by its Name, TIN, Email or Internal Reference.")
    employee_id = fields.Many2one('hr.employee', string="Employee", default=_default_employee, required=True, ondelete='cascade', index=True)
    active = fields.Boolean(string="Enable",default=True, help="Set active to false to hide the rebate contract without removing it.")
    date_start = fields.Datetime(string="Contract start date")
    date_end = fields.Datetime(string="Contract end date")
    bonus_money = fields.Float("Bonus money")
    reward_criteria = fields.Text("Reward criteria")
    remark = fields.Text("Remark")
    target = fields.Char("Target")
    product_target = fields.Char("Product target")
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)



    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('x.partner.rebate') or _('New')
        result = super(PartnerRebate, self).create(vals)
        return result

    @api.model
    def _default_organization_id(self):
        return self.env.user.x_organization_id and self.env.user.x_organization_id.id
