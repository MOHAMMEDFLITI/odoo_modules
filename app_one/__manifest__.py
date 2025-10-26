{
     'name': 'app_one',
     'author' : 'mohammed FLITI ',
     'category': 'realty',
     'version': '1.0',
     'depends': ['base','sale_management','account','mail','contacts'],
     'data': [
         'security/ir.model.access.csv',
         'security/security.xml',
         'data/sequence.xml',
         'reports/property_report.xml',
         'wizard/change_state_wizard_view.xml',
         'views/base_menu.xml',
         'views/property_view.xml',
         'views/owner_view.xml',
         'views/tag_view.xml',
         'views/sale_order_view.xml',
         'views/res_partner_view.xml',
         'views/building.xml',
         'views/property_history_view.xml',
         'views/upgrade_app_view.xml',
         'views/account_move_view.xml',
         
         
         
    ],
    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css',
        ],
        'web.report_assets_common': [
            'app_one/static/src/css/fonts.css',
        ],
    },
    'application': True


}