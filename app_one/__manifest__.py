{
     'name': 'Real Estate',
     'author' : 'mohammed FLITI ',
     'category': 'realty',
     'version': '1.0',
     'depends': ['base','sale_management','mail','contacts'],
     'data': [
         'security/ir.model.access.csv',
         'views/base_menu.xml',
         'views/property_view.xml',
         'views/owner_view.xml',
         'views/tag_view.xml',
         'views/sale_order_view.xml',
         'views/res_partner_view.xml',
         'views/building.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_one/static/src/css/property.css',
        ],
    },
    'application': True


}