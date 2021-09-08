import logging
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _default_founding_year(self):
        return str(fields.Date.today().year)

    @api.model
    def _default_transaction_classification(self):
        return self.env["x.transaction.classification"].search([("default", "=", True)]).ids

    @api.model
    def _default_department_classification(self):
        return self.env["x.department.classification"].search([("default", "=", True)]).ids

    x_contact_classification = fields.Selection([
        ("other", "Other"), ("customer", "Customer"), ("supplier", "Supplier")
    ], string="Contact Classification", required=True, default="other")
    x_partner_code = fields.Char(string="Partner Code")

    x_transaction_classification = fields.Many2many("x.transaction.classification",
                                                    default=_default_transaction_classification,
                                                    string="Transaction Classification")
    x_department = fields.Selection(
        [("industrial", "Industrial/ Medical Gas"), ("lpg", "LP Gas")],
        string="Department"
    )
    x_transaction_basic_contract = fields.Selection(
        [("yes", "Conclusion"), ("no", "Do not Conclude"), ("never", "Not applicable")],
        string="Transaction Basic Contract", required=True, default="yes"
    )
    x_contract_not_apply_reason = fields.Text(
        string="Reason"
    )
    x_fax_number = fields.Char(
        string="Fax Number", size=20
    )
    x_payment_notice_fax_number = fields.Char(
        string="Payment Notice Fax Number", size=20
    )
    x_founding_year = fields.Char(string="Founding Year", default=_default_founding_year)
    x_capital = fields.Monetary(string="Capital", currency_field="currency_id")
    x_partner_performance = fields.One2many(
        comodel_name="x.partner.sales.information", inverse_name="partner_id",
        string="Performance Information"
    )
    x_show_construction_permit = fields.Boolean(
        string="Show Construction Permit", compute="_compute_x_show_construction_permit",
        help="This is a technical field, to indicate whether or not construction permit "
             "should be shown on form"
    )
    x_partner_construction_permit = fields.One2many(
        comodel_name="x.x_partner.partner_construction_permit", inverse_name="partner_id",
        string="Construction Permit"
    )
    x_payment_term_using = fields.Selection(
        selection=[("regular", "Our Regulations (See detail regulation)"), ("other", "Others")],
        string="Payment Term", required=True, default="regular"
    )
    x_other_payment_term = fields.Char(string="Other Payment Term")
    x_reason_to_change_payment_term = fields.Text(string="Reason for Fluctuation")
    x_control_account = fields.Many2one(
        comodel_name="account.account", string="Control Account"
    )
    x_sale_area = fields.Char(string="Sale Area")
    x_minimum_sale = fields.Monetary("Minimum Sales", currency_field="currency_id", copy=False)
    x_receipt_place = fields.Many2one(
        comodel_name="stock.location", string="Receipt Location",
        ondelete="restrict", copy=False
    )
    x_purchase_person_id = fields.Many2one(
        comodel_name="res.users", string="Purchase Person", domain=[('share', '=', False)]
    )
    x_purchase_area = fields.Char(string="Purchase Area")
    x_minimum_purchase = fields.Monetary("Minimum Purchase", currency_field="currency_id", copy=False)
    x_delivery_place = fields.Many2one(
        comodel_name="stock.location", string="Delivery Location",
        ondelete="restrict", copy=False
    )

    @api.depends("x_transaction_classification")
    def _compute_x_show_construction_permit(self):
        gas_equipment_id = self.env.ref("x_partner.transaction_classification_gas_equipment").id
        for r in self:
            r.x_show_construction_permit = gas_equipment_id in r.x_transaction_classification.ids

    def name_get(self):
        res = dict(super(ResPartner, self).name_get())
        final = []
        for _id in res.keys():
            record = self.browse(_id)
            name = "[%s] %s" % (record.x_partner_code, res[_id]) if record.x_partner_code else res[_id]
            final.append((_id, name))
        return final

