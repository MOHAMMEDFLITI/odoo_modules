from odoo import models,fields,api

class Property(models.Model):
    _name='property'
    _description='Property record'
    _inherit = ['mail.thread','mail.activity.mixin']
    name = fields.Char(required=True,default="new",size=5)
    descreption = fields.Text(tracking=True)
    postcode = fields.Char(required=True)
    ref = fields.Char(default='nv',readonly=True)
    date_availability = fields.Date(tracking=True)
    expected_selling_date = fields.Date(required=True)
    is_late = fields.Boolean()
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
    
    def search(self, args, offset=0, limit=None, order=None): # there is no parameter called count anymore (Odoo 18 removed it) also access_rights is removed
        print("in search method")
        res = super(Property, self).search(args, offset=offset, limit=limit, order=order) # super.search([]) → returns a recordset  ||  super._search([]) → returns a list of IDs
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
            rec.create_history_record(rec.state, 'draft')
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.create_history_record(rec.state, 'pending')
            rec.write({'state':'pending'})

    def action_sold(self):
        for rec in self:
            rec.create_history_record(rec.state, 'sold')
            rec.state = 'sold'
            
    def action_closed(self):
        for rec in self:
            rec.create_history_record(rec.state, 'closed')
            rec.state = 'closed'

    def check_expected_selling_date(self):
      # print(self)  #property()
        property_ids = self.search([])
        for rec in property_ids:
            #print(rec) # 1 3 8 if using _search else return objects
            #print(rec.expected_selling_date) # 2025-10-05 and so on
            if rec.state != 'sold':
                if rec.expected_selling_date and rec.expected_selling_date < fields.Date.today():
                    rec.is_late = True

                

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
            
    def action(self):
        #print(self.env.user.name)
        #print(self.env.company.name)
        #print(self.env.context)
        #print(self.env.context.get('tz'))
        # print(self.env.uid)
        # print(self.env.cr)
        #print(self.env['owner'].search([]))
        print(self.env['owner'].create({'name':'owner from env','phone':'123456'}))

    
    @api.model
    def create(self,vals):
        res = super(Property,self).create(vals)
        if res.ref == 'nv':
            seq = self.env['ir.sequence'].next_by_code('property_seq')
            res.ref = seq
        return res
    
    def create_history_record(self, old_state, new_state,reason='nothing'):

            self.env['property.history'].create({
                'user_id': self.env.uid,
                'property_id': self.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason,
            })
    def action_open_change_state_wizard(self):
        action = self.env.ref('app_one.change_state_wizard_action')
        action = action.read()[0]  # Convert record to dict for return
        action['context'] = {
            'default_property_id': self.id,
        }
        return action


            


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


