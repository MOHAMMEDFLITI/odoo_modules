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

    @api.constrains('date_av')
    def _check_date_av(self):
        for record in self:
            if record.date_av < fields.Date.today():
                raise models.ValidationError("The date cannot be in the paste.")
                #print("The date cannot be in the paste.")

    _sql_constraints = [
        ('unique_ref','unique(ref)','this ref is exist'),
    ]