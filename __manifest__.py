# -*- coding: utf-8 -*-
{
    'name': "Book Library",

    'summary': "Modul Perpustakaan",

    'description': """
Book Library Study Case
    """,

    'author': "Rimba Sahara",
    'website': "https://rimbashr.my.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/book_views.xml',
        'views/member_views.xml',
        'views/rent_transaction_views.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

