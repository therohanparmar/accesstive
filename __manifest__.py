{
    'name': 'Accesstive - Accessibility Assistant',
    'version': '1.0.0',
    'summary': 'Accesstive accessibility assistant widget integration for Odoo websites',
    'description': """
        Accesstive is an all-in-one accessibility platform that helps websites become
        inclusive, compliant, and user-friendly. This addon integrates the Accesstive
        assistant widget into your Odoo website, providing AI-based live audits,
        monitoring, and an intelligent accessibility assistant.

        Features:
        - Automatic injection of Accesstive assistant script
        - Backend configuration options
        - Enable/disable accessibility widget
        - Compatible with Odoo 18 and 19
    """,
    'author': 'Accesstive',
    'website': 'https://www.accesstive.com',
    'category': 'Website',
    'license': 'LGPL-3',
    'depends': ['base', 'website'],
    'data': [
        'templates/website_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}