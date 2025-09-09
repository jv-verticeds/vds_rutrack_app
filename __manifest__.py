# -*- coding: utf-8 -*-
{
    'name': "vds_rutrack_app",
    'summary': "Módulo de Odoo para vds_rutrack_app",
    'description': """
        Módulo de Odoo para vds_rutrack_app
    """,
    'author': "VDS",
    'website': "http://www.verticeds.com",
    'icon': 'vds_rutrack_app/static/description/icon.png',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
