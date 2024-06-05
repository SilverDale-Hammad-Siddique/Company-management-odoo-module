from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Employees(models.Model):
    _inherit = 'hr.employee'

    employee_idd = fields.Many2one("hr.employee")
    active = fields.Boolean(string="Active", default=True)
    my_employee = fields.Boolean(string="My Employee", default=True)
    department_idd = fields.Many2one('department', string="Department")
    company_idd = fields.Many2one('company', string="Company")
    phone = fields.Char(string='Phone')

    def action_share_whatsapp(self):
        # if not self.employee_idd.phone:
        #     raise ValidationError(_("Missing phone in company record"))
        message = 'Hi %s' % self.employee_idd.name
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.employee_idd.phone, message)

        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url
        }

    def action_print_employee_report(self):
        # The actual logic for generating and returning the report should be implemented here
        pass
