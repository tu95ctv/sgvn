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
        "hr", "purchase_stock", "sales_team"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/company.xml",
        "views/purchase.xml",
    ],
    "application": False,
    "installable": True,
}
