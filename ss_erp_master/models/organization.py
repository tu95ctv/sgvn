# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Organization(models.Model):
    _name = 'ss_erp.organization'
    _description = 'Organization'
    _parent_name = "parent_id"
    _parent_store = True
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']

    name = fields.Char(string='Name')
    company_id = fields.Many2one(
        'res.company', string='Company', required=True,
        readonly=True, default=lambda self: self.env.company)
    sequence = fields.Integer("Sequence")
    active = fields.Boolean(default=True, help="If the active field is set to False, it will allow you to hide the payment terms without removing it.")
    expire_start_date = fields.Datetime(string="Valid start date", copy=False)
    expire_end_date = fields.Datetime(string="Expiration date", copy=False)
    child_ids = fields.One2many('ss_erp.organization', 'parent_id', string="Contains Organizations", ondelete="restrict",)
    parent_path = fields.Char(index=True)
    code = fields.Char(string="Organization Code", required=True, copy=False)
    organization_category_id = fields.Many2one("ss_erp.organization.category", string="Organization category")
    parent_id = fields.Many2one("ss_erp.organization", string="Parent organization", )
    parent_organization_code = fields.Char(string="Parent organization code", compute="_compute_parent_organization_code")
    organization_country_id = fields.Many2one("res.country", string="Organization address / country")
    organization_zip = fields.Char(string="Organization address / zip code")
    organization_state_id = fields.Many2one("res.country.state", string="Organization address / prefecture")
    organization_city = fields.Char("Organization Address / City")
    organization_street = fields.Char("Organization address / town name")
    organization_street2 = fields.Char("Organization address / town name address 2")
    organization_phone = fields.Char("Organization phone number")
    organization_fax = fields.Char("Organization Representative Fax")

    @api.depends('parent_id', 'parent_id.code')
    def _compute_parent_organization_code(self):
        for record in self:
            record.parent_organization_code = record.parent_id.code if record.parent_id else ''

    @api.constrains("expire_start_date", "expire_end_date")
    def _check_dates(self):
        """End date should not be before start date, if not filled

        :raises ValidationError: When constraint is violated
        """
        for record in self:
            if (
                record.expire_start_date
                and record.expire_end_date
                and record.expire_start_date > record.expire_end_date
            ):
                raise ValidationError(
                    _("The starting date cannot be after the ending date.")
                )

    @api.constrains('child_ids')
    def _check_recursion(self):
        if not self._check_m2m_recursion('child_ids'):
            raise ValidationError(_('Recursion found in child server actions'))
