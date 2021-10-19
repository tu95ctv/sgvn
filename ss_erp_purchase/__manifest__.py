# -*- coding: utf-8 -*-
{
    "name": "SGVN Purchase",
    "summary": """
        SGVN Purchase Quotation
    """,
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "website": "https://latido.vn",
    "author": "LATIDO",
    "depends": [
        "ss_erp_master", "purchase_stock", "sales_team"
    ],
    "data": [
        # SECURITY
        "security/ir.model.access.csv",
        # DATA
        # VIEWS
        "views/res_company_views.xml",
        "views/product_template_views.xml",
        "views/purchase_order_views.xml",
        # REPORTS
        # "reports/action.xml",
        # "reports/layout.xml",
        # "reports/quotation_request_template_report.xml",
        # "reports/estimate_request_template_report.xml",
        # # MAIL TEMPLATE
        # "data/mail_template_data.xml",
    ],
    "application": False,
    "installable": True,
}
