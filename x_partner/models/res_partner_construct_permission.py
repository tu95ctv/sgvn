from odoo import _, api, fields, models


class PartnerConstructionPermit(models.Model):
    _name = "x.x_partner.partner_construction_permit"
    _description = "Partner Construction Permit"
    
    name = fields.Char(string="Permission Number", required=True)
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Contact", domain="[('company_type', '=', 'company')]",
        readonly=True, copy=False, ondelete="cascade", required=True
    )
    x_construction_permit_type_id = fields.Char(
        string="Type of Permission", required=True
    )
    x_authorize_classification = fields.Char(
        string="Misnister/ Governor Classification", required=True
    )
    x_type_classification = fields.Char(
        string="Specific/ General Classification", required=True
    )
    x_permission_date = fields.Date(string="Permission Date", default=fields.Date.today)
