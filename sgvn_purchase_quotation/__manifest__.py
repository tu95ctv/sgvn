# -*- coding: utf-8 -*-
{
    "name": "SGVN Purchase Quotation",
    "summary": """
        SGVN Purchase Quotation
    """,
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "website": "https://latido.vn",
    "author": "LATIDO",
    "depends": [
        "x_company_organization", "purchase_stock", "sales_team", "x_partner"
    ],
    "data": [
        # SECURITY
        "security/ir.model.access.csv",
        # DATA
        "data/transaction_classification_data.xml",
        # VIEWS
        "views/company.xml",
        "views/purchase.xml",
        "views/partner.xml",
        # REPORTS
        "reports/action.xml",
        "reports/layout_quotation_request_report.xml",
        "reports/layout_estimate request_report.xml",
        "reports/quotation_request_template_report.xml",
        "reports/estimate_request_template_report.xml",

    ],
    "application": False,
    "installable": True,
}
