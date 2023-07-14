# -*- coding: utf-8 -*-
{
    'name': "Customer rating management",  # Module title
    'summary': "Customer rating management",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['sale','sale_management','purchase'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/customer.xml',
        'views/sales.xml',
        'views/purchase.xml'
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}


