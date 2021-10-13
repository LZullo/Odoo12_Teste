# -*- coding: utf-8 -*-
{
    'name': "TestOdoo",

    'summary': """
        TestOdoo
        """,

    'description': """
        
    """,

    'author': "Leticia Zullo",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'views/views.xml',
        'report/crm_customer_report.xml',
        'report/crm_customer_print.xml',

    ],



}