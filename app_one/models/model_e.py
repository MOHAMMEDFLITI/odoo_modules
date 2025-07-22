from odoo import models,fields

class ModelE(models.Model):
    _name = False
    date_av = fields.Date()
    isShadow = fields.Boolean()
    orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ])