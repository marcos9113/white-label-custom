# noinspection PyStatementEffect
{
    'name': "Gamerun White Label",
    'version': '18.0.1.0.3',
    'author': "Gamerun",
    'category': 'Debranding',
    'summary': "Debrand Gamerun ERP",
    'description': """
Debrand Gamerun ERP
    """,
    'website': 'https://gamerun.ai',
    'depends': [
        'base',
        'base_setup',
        'web',
        'mail',
        'mail_bot',
        'base',
        'web_tour',
    ],
    'external_dependencies': {'python': ['lxml']},
    'data': [
        'pre_install.xml',
        'data/data.xml',
        'views/views.xml',
        'views/res_config.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'gamerun_whitelabel/static/src/css/web.css',
            'gamerun_whitelabel/static/src/js/base.js',
            'gamerun_whitelabel/static/src/js/dialog.js',
            'gamerun_whitelabel/static/src/js/field_upgrade.js',
            'gamerun_whitelabel/static/src/js/user_menu_items.js',
            'gamerun_whitelabel/static/src/js/translation.js',
        ],
    },
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'license': 'LGPL-3',
}
