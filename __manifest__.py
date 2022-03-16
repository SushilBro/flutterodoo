# -*- coding: utf-8 -*-
{
    'name' : 'Flutter Login System',
    'version' : '1.0',
    'summary': 'Samagyan Login System',
    'sequence': 10,
    'description': """Flutter odoo server""",
    'category': 'Sales/Sales',
    'website': 'https://www.hotellila.com',
    'depends' : ['base'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/signUP_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
