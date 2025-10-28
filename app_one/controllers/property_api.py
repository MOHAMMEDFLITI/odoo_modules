from odoo import http
from odoo.http import request
import json
class PropertyApi(http.Controller):
    @http.route('/v1/app_one/property', type='http', auth='none', methods=['POST'], csrf=False)
    def post_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        print('Received json for new property:', vals)
        #print('Received args for new property:', args)
        # the difference between args and vals is that args is a string while vals is a dictionary
        res = request.env['property'].sudo().create(vals)
        # sudo() to bypass access rights
        if res:
            print('Created property ', res)
            return request.make_json_response({'message': 'property has been created successfully', 'property_id': res.id}, status=200)
       
