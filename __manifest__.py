# -*- coding: utf-8 -*-
{
    'name': "MDA HR Extension",

    'summary': "MDA HR Extension for MDAs",

    'description': """
Long description of module's purpose
    """,

    'author': "Tani Nigeria Ltd",
    'website': "https://www.wawa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','contacts',],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/import_lga_menu.xml',
        'views/hr_employee_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

