from odoo import http

class TestApi(http.Controller):
    @http.route('/v1/app_one/test', type='http', auth='none', methods=['GET'], csrf=False)
    def test_endpoint(self, **kwargs):
        print('This is a test API endpoint from app_one.')


# db_name = db_test
# if you do requests from postman without headers, you need to add "db_name" in odoo.conf
