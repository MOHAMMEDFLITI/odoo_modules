from odoo import models,fields,api

class Property(models.Model):
    _name='property'
    _description='Property record'
    _inherit = ['mail.thread','mail.activity.mixin']
    name = fields.Char(required=True,default="new",size=5)
    descreption = fields.Text(tracking=True)
    postcode = fields.Char(required=True)
    date_availability = fields.Date(tracking=True)
    expected_price = fields.Float(digits=(0,5))
    sold_price = fields.Float()
    diff = fields.Float(compute='_compute_diff', store=True ,readonly=0)
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

    line_ids = fields.One2many('property.line','property_id')
    other_line = fields.One2many('property.other.line','propertyy_id')
    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
        ('closed','Closed'),
    ], default='draft')

    owner_id = fields.Many2one("owner")
    owner_adress = fields.Char(related='owner_id.adress',store=True, readonly=0) # must be same field type as the field in the related model
    owner_phone = fields.Char(related='owner_id.phone',store=True)
    tag_ids = fields.Many2many("tag")

    # if you have already record that disrespect the constraint so this constraint will not be applied and to fix it you have to delete the record that disrespect the constraint
    # if you have already app and you want to do constraint so use the other level of constraint
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
    

    def action_draft(self):
        for rec in self:
            print("in action_draft method")
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            print("in action_pending method")
            rec.write({'state':'pending'})

    def action_sold(self):
        for rec in self:
            print("in action_sold method")
            rec.state = 'sold'
            
    def action_closed(self):
        for rec in self:
            rec.state = 'closed'

    @api.depends('expected_price','sold_price','owner_id.phone')
    # depends on simple fields (views fields or model fields) or relational fields (many2one, many2many, one2many)
    def _compute_diff(self):
        for rec in self:
            print("in _compute_diff method")    
            rec.diff = rec.expected_price - rec.sold_price

    @api.onchange('garden')
    # onchange works only in views fields
    def _onchange_garden(self):
        for rec in self:
            print("in _onchange_garden method")
            if rec.garden == False:
                rec.garden_area = 0

    @api.onchange('bedrooms')
    def _onchange_bedrooms(self):
        for rec in self:
            print("in _onchange_bedrooms method")
            if rec.bedrooms < 0:
                return {
                    'warning':{
                        'title':'wrong value',
                        'message':'the number of bedrooms cannot be negative',
                        'type':'notification'
                    },
                    'value':{
                        'bedrooms':0
                    }
                }
            


class PropertyLine(models.Model):
    _name='property.line'
    _description='Property line record'

    property_id=fields.Many2one('property')
    description=fields.Char()
    area=fields.Float()
    price=fields.Float()
    date=fields.Date()

class PropertyOtherLine(models.Model):
    _name='property.other.line'


    propertyy_id = fields.Many2one('property')
    name = fields.Char()
    value = fields.Float()
    yes_no = fields.Boolean()
    notes = fields.Text()


