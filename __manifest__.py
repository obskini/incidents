{
    'name': 'Status Dashboard',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Status dashboard for Accomodata infrastructure',
    'description': 'This module provides a custom status dashboard.',
    'author': 'Obe Conil',
    'depends': ['base'],
    'data': [
        'views/status_dashboard_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'icon': 'incidents/static/description/icon.png',
    'license': 'LGPL-3',
}
