from odoo import models, fields




class ChangeStateWizard(models.TransientModel):

    _name = 'change.state.wizard'
    _description = 'Wizard to Change State'

    property_id = fields.Many2one('property')
    new_state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
    ],default='draft')
    reason = fields.Text(string='Reason for State Change')

    def apply_change(self):
        print("inside apply_change method")
        if self.property_id:
            old_state = self.property_id.state
            self.property_id.state = self.new_state
            self.property_id.create_history_record(old_state, self.new_state,self.reason)