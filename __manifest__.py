# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Query Tool',
    'version': '12.0.0.1.1',
    'category': 'Sale',
    'summary': 'Query Tool',
    'author': 'Roberto Zanardo',
    'website': 'https://www.robertozanardo.com/',
    'description': """

Direct Query Tool for Odoo
===========================

Useful to make db operations:Use at your own risk.

Add a Query function under technical settings, it allows to run query directly on current Odoo database. 
It allows also to save some query and create unlimited query templates. Use it at your own risk!

Roberto
www.robertozanardo.com

""",
    'depends': ['base'],
    'data': [
        'data/data.xml',
        'views/querytool.xml',
        'security/ir.model.access.csv',
        ],
    'installable': True,
    'auto_install': False,
    "application": False,
}
