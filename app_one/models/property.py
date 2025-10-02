from odoo import models,fields,api

class Property(models.Model):
    _name='property'

    name = fields.Char(required=True,default="new",size=5)
    descreption = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date()
    expected_price = fields.Float(digits=(0,5))
    sold_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ], default='north')
    owner_id = fields.Many2one("owner")
    tag_ids = fields.Many2many("tag")

    _sql_constraints = [
        ('unique_name','unique(name)','this name is exist'),
    ]

    @api.constrains('date_availability')
    def _check_date_av(self):
        for record in self:
            if record.date_availability < fields.Date.today():
                raise models.ValidationError("The date cannot be in the paste.")

    @api.model_create_multi
    def create(self,vals):
        print("in create method")
        res = super(Property,self).create(vals)
        return res
    
    def search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        print("in search method")
        res = super(Property, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
        return res

    

    def write(self,vals):
        print("in write method")
        res = super(Property,self).write(vals)
        return res
    

    def unlink(self):
        print("in unlink method")
        res = super(Property,self).unlink()
        return res