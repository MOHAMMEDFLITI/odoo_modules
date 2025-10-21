from odoo import models,fields

class PropertyHistory(models.Model):
    _name='property.history'
    _description='Property history'

    user_id = fields.Many2one('res.users')
    property_id = fields.Many2one('property')
    old_state = fields.Char()
    new_state = fields.Char()
    change_date = fields.Datetime(default=fields.Datetime.now)
    reason = fields.Char()



