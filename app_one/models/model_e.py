from odoo import models,fields,api

class ModelE(models.Model):
    _name='model.e'
    ref = fields.Char(size=3)
    date_av = fields.Date()
    isShadow = fields.Boolean(required=True,default=False)
    orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ])
# on float we can use digits=(total,decimals)

# there is three validation levels:
# 1- logic tier for exemple: constraints
# 2- presentation tier for exemple: attrs in views
# 3- databaser tier for exemple: 
# required=True in fields in logic and database tier

    _sql_constraints = [
        ('unique_ref','unique(ref)','this ref is exist'),
    ]

    @api.constrains('date_av')
    def _check_date_av(self):
        for record in self:
            if record.date_av < fields.Date.today():
                raise models.ValidationError("The date cannot be in the paste.")
                #print("The date cannot be in the paste.")

    @api.model_create_multi
    def create(self,vals):
        print("in create method")
        res = super(ModelE,self).create(vals)
        return res
    
    def search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        print("in search method")
        res = super(ModelE, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
        return res

    

    def write(self,vals):
        print("in write method")
        res = super(ModelE,self).write(vals)
        return res
    

    def unlink(self):
        print("in unlink method")
        res = super(ModelE,self).unlink()
        return res