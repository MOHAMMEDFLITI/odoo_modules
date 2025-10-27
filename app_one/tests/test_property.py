from odoo.tests.common import TransactionCase


class TestProperty(TransactionCase):
    def setUp(self,*args, **kwargs):
        super(TestProperty,self).setUp()

        self.property_one = self.env['property'].create({
            'name': 'Property One',
            'ref': 'PROP',
            'description': 'A property created for testing functionality.',
            'postcode': '12345',
            'bedrooms': 3,
        })

    def test_one_property_values(self):
        property_id = self.property_one
        self.assertRecordValues(property_id, [{
            'name': 'Property One',
            'ref': 'PROP',
            'description': 'A property created for testing functionality.',
            'postcode': '12345',
            'bedrooms': 3,
        }])