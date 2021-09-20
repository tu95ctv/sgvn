# -*- coding: utf-8 -*-
{
    "name": "SGVN VLA Base",
    "summary": """
        SGVN VLA Base
    """,
    "version": "14.0.1.0.0",
    "category": "Purchase",
    "website": "https://latido.vn",
    "author": "LATIDO",
    "depends": [
        "x_company_organization", "x_partner"
    ],
    "data": [
        # SECURITY
        "security/ir.model.access.csv",
        # DATA
        # VIEWS
        # REPORTS

    ],
    "application": False,
    "installable": True,
    'pre_init_hook': 'pre_init_hook',
    'uninstall_hook': 'uninstall_hook',

}
