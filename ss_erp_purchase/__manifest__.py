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
        "ss_erp_master", "purchase_stock", "sales_team", "ss_erp_base"
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
        "reports/action.xml",
        # "reports/layout.xml",
        "reports/purchase_quotation_report.xml",
        "reports/purchase_quotation_for_construction_report.xml",
        "reports/purchase_order_template_report.xml",
        # # MAIL TEMPLATE
        # "data/mail_template_data.xml",
    ],
    "application": False,
    "installable": True,
}
