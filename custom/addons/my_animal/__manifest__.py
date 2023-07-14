# -*- coding: utf-8 -*-
{
    'name': "My Animal",  # Module title
    'summary': "Manage animal easily",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base', 'my_library'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/animal.xml',
    ],
    # This demo data files will be loaded if db initialize with demo data (commented becaues file is not added in this example)
    # 'demo': [
    #     'demo.xml'
    # ],
}
