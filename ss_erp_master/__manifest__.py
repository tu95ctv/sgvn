# -*- coding: utf-8 -*-
{
    "name": "SS ERP Master",
    "summary": """
        SS ERP Master
    """,
    "version": "14.0.1.0.0",
    "category": "Human Resources/Employees",
    "website": "https://latido.vn",
    "author": "LATIDO",
    "depends": [
        "mail",
        "contacts"
    ],
    "data": [
        # SECURITY
        "security/ir.model.access.csv",
        # DATA
        "data/bis_category_data.xml",
        # VIEWS
        "views/responsible_department_views.xml",
        "views/organization_views.xml",
        "views/organization_category_views.xml",
        "views/res_partner_views.xml",
        "views/res_users_views.xml",
        # REPORTS

    ],
    "application": False,
    "installable": True,
}
