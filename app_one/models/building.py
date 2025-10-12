from odoo import models,fields

class building(models.Model):
    _name='building'
    _description='Building record'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'code' # bigger priority than name field


    no = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    name = fields.Char() # reserved field 
    active = fields.Boolean(default=True) # to archive the record




