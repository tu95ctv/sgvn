# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResponsibleDepartment(models.Model):
    _name = 'ss.erp.responsible.department'

    name = fields.Char(string='Name')
    company_id = fields.Many2one(
        'res.company', string='Company',required=True,
        readonly=True, default=lambda self: self.env.company)
    sequence = fields.Integer("Sequence")
    active = fields.Boolean(default=True, help="If the active field is set to False, it will allow you to hide the payment terms without removing it.")
    date_start = fields.Datetime(string="Valid start date", copy=False)
    date_end = fields.Datetime(string="Expiration date", copy=False)
    
    
    @api.constrains("date_start", "date_end")
    def _check_dates(self):
        """End date should not be before start date, if not filled

        :raises ValidationError: When constraint is violated
        """
        for record in self:
            if (
                record.date_start
                and record.date_end
                and record.date_start > record.date_end
            ):
                raise ValidationError(
                    _("The starting date cannot be after the ending date.")
                )