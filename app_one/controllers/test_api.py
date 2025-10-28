from odoo import http

class TestApi(http.Controller):
    @http.route('/app_one/test', type='http', auth='none', methods=['GET'], csrf=False)
    def test_endpoint(self, **kwargs):
        print('This is a test API endpoint from app_one.')