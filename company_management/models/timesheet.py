from odoo import models, fields, api


class TimeSheet(models.Model):
    _name = 'time.sheet.employee'

    date = fields.Date(string='Date')

    employee_idd = fields.Many2one('hr.employee', string='Employee', compute='_compute_employee_idd', store=True,
                                   tracking=True)
    project_idd = fields.Many2one('project', string='Project', required=True, tracking=True)
    task_idd = fields.Many2one('task', string='Task', tracking=True)
    name = fields.Char(string='Description', tracking=True)
    unit_amount = fields.Float(string='Hours Spent', tracking=True)
    description = fields.Html(string="Description")
    amount = fields.Float(string="Amount")
    company_idd = fields.Many2one('company', string='Company', invisible=True, tracking=True)

    @api.depends('task_idd.employee_ids')  # Change the dependency field to 'task_idd.employee_ids'
    def _compute_employee_idd(self):
        for timesheet in self:
            # Assuming only one employee is selected as assignee for simplicity
            timesheet.employee_idd = timesheet.task_idd.employee_ids[:1]  # Select the first employee in the list
