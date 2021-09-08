from odoo import fields, models


class DepartmentClassification(models.Model):
    _name = "x.department.classification"
    _description = "Department Classification"

    name = fields.Char("Transaction")
    default = fields.Boolean("Default?")
    description = fields.Char("Note fields")
