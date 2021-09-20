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
        # "data/transaction_classification_data.xml",
        # VIEWS
        "views/product_product_views.xml",
        "views/purchase_views.xml",
        "views/res_config_settings_views.xml",
        # WIZARDS
        "wizards/purchase_confirm_wiz_view.xml",
        # REPORTS
        # MAIL TEMPLATE
        # "data/mail_template_data.xml",
    ],
    "application": False,
    "installable": True,
}
