# -*- coding: utf-8 -*-
{
    "name": "SGVN Purchase Order",
    "summary": """
        SGVN Purchase Order
    """,
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "website": "https://latido.vn",
    "author": "LATIDO",
    "depends": [
        "x_purchase_quotation"
    ],
    "data": [
        # SECURITY
        "security/purchase_security.xml",
        "security/ir.model.access.csv",
        # DATA
        # VIEWS
        "views/product_product_views.xml",
        "views/purchase_views.xml",
        "views/res_config_settings_views.xml",
        # WIZARDS
        "wizards/purchase_confirm_wiz_view.xml",
        # REPORTS
        "reports/action.xml",
        "reports/layout.xml",
        "reports/purchase_order_construction_template_report.xml",
        "reports/purchase_order_template_report.xml",
        # MAIL TEMPLATE
        "data/mail_template_data.xml",
    ],
    "application": False,
    "installable": True,
}
