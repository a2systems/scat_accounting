{
    'name': 'SCAT Accounting',
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'account',
    ],
    'data': [
             'views/account_move_view.xml',
             'views/account_account_view.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
