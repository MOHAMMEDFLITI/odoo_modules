from odoo import models,fields


# there are 2 types of inheritance in odoo

# 1- model inheritance ('tradional' using "_inherit or _inherit _name" and 'delegation' using "_inherits")
# 2- view inheritance (xml files)


class SaleOrder(models.Model):
    _inherit='sale.order'

    property_id=fields.Many2one('property')

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print("in action_confirm method")
        return res



# TODO : fixing "upgrade odoo server"  + xml view