# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Query Tool',
    'version': '14.0.0.1.1',
    'category': 'Utilities',
    'summary': 'Query Tool',
    'author': 'Roberto Zanardo',
    'website': 'https://www.robertozanardo.com/',
    'description': """

Direct Query Tool for Odoo
===========================

Useful to make db operations:Use at your own risk.

Add a Query function under technical settings, it allows to run query directly on current Odoo database. 
It allows also to save some query and create unlimited query templates. 

It supports also multiple query separated by ;
Example:
DELETE FROM fob_order;
DELETE FROM fob_po_order;
DELETE FROM account_invoice;

Use it at your own risk!
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
