# -*- coding: utf-8 -*-
{
    "name": "SGVN Rebate Management",
    "summary": """
        SGVN Rebate Management
    """,
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "website": "https://latido.vn",
    "author": "LATIDO",
    "depends": [
        "x_company_organization", "x_partner", "purchase", "account"
    ],
    "data": [
        # SECURITY
        "security/ir.model.access.csv",
        "security/rebate_security.xml",
        # DATA
        "data/ir_sequence_data.xml",
        "data/ir_action_server_data.xml",
        "data/ir_cron_data.xml",
        # VIEWS
        "views/partner_rebate_views.xml",
        "views/webclient_templates.xml",
        # WIZARDS
        "wizards/partner_rebate_attachment_wizard_views.xml",
        # REPORTS

    ],
    "application": False,
    "installable": True,
}
