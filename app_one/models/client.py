from odoo import models

class Client(models.Model):
    _name='client'
    _inherit = 'owner'



# client will have all fields of owner + its own fields