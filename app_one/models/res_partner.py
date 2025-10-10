from odoo import models,fields,api




class ResPartner(models.Model):
    _inherit='res.partner'


    property_id = fields.Many2one('property')

    # if i add store=True we must add depends decorator
    
    #price = fields.Float(compute='_compute_price',store=True)


    # @api.depends('property_id')
    # def _compute_price(self):
    #     for self in self:
    #         if self.property_id:
    #             self.price = self.property_id.expected_price
    #         else:
    #             self.price = 0



    # better methode
    price = fields.Float(related='property_id.expected_price')