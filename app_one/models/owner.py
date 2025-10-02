from odoo import models,fields

class Owner(models.Model):
    _name='owner'

    name = fields.Char(required=True,default="new")
    adress = fields.Char()
    phone = fields.Char()
    property_ids = fields.One2many("property","owner_id")

    # one to many (reverse) and many to many (new table : nameT1_nameT2_rel) does not create a column in the table