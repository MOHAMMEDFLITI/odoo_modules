from odoo import http
from odoo.http import request
import json
class PropertyApi(http.Controller):
    @http.route('/v1/app_one/property', type='http', auth='none', methods=['POST'], csrf=False)
    def post_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
       # print('Received json for new property:', vals)
        #print('Received args for new property:', args)
        # the difference between args and vals is that args is a string while vals is a dictionary
        if not vals.get('name'):
            return request.make_json_response({
                'error': 'Property name is required'
                }, status=400)
        try:
            res = request.env['property'].sudo().create(vals)
            # sudo() to bypass access rights
            if res:
              #  print('Created property ', res)
                return request.make_json_response({
                    'message': 'property has been created successfully',
                    'property_id': res.id,
                        'property_name': res.name
                        }, status=201)
        except Exception as e:
          #  print('Error creating property:', str(e))
            return request.make_json_response({
                'error': 'Failed to create property',
                'details': str(e)
                }, status=400)
        

    @http.route('/v1/app_one/property_json', type='json', auth='none', methods=['POST'], csrf=False)
    # json : accept only json type in body request 
    def post_property_json(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['property'].sudo().create(vals)
        if res:
            return [
                {
                    'message': 'property has been created successfully',
                      
                      }
                ]
        
    @http.route('/v1/app_one/property/<int:property_id>', type='http', auth='none', methods=['PUT'], csrf=False)
    def update_property(self, property_id):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        property_record = request.env['property'].sudo().browse(property_id)
        if not property_record.exists():
            return request.make_json_response({
                'error': 'Property not found'
                }, status=404)
        try:
            property_record.sudo().write(vals)
            return request.make_json_response({
                'message': 'Property has been updated successfully',
                'property_id': property_id
                }, status=200)
        except Exception as e:
            return request.make_json_response({
                'error': 'Failed to update property',
                'details': str(e)
                }, status=400)
        

    @http.route('/v1/app_one/property/<int:property_id>', type='http', auth='none', methods=['GET'], csrf=False)
    def get_property(self, property_id):
        try :
            property_record = request.env['property'].sudo().browse(property_id)
            if not property_record.exists():
                return request.make_json_response({
                    'error': 'Property not found'
                    }, status=404)
            property_data = {
                'id': property_record.id,
                'name': property_record.name,
                'expected_price': property_record.expected_price,
                'bedrooms': property_record.bedrooms,
                'garden': property_record.garden,
                'state': property_record.state,
            }
            return request.make_json_response(property_data, status=200)
        except Exception as e:
            return request.make_json_response({
                'error': 'Failed to get property',
                'details': str(e)
                }, status=400)
        
    @http.route('/v1/app_one/property/<int:property_id>', type='http', auth='none', methods=['DELETE'], csrf=False)
    def delete_property(self, property_id):
        try:
            property_record = request.env['property'].sudo().browse(property_id)
            if not property_record.exists():
                return request.make_json_response({
                    'error': 'Property not found'
                    }, status=404)
            property_record.sudo().unlink()
            return request.make_json_response({
                'message': 'Property has been deleted successfully',
                'property_id': property_id
                }, status=200)
        except Exception as e:
            return request.make_json_response({
                'error': 'Failed to delete property',
                'details': str(e)
                }, status=400)
