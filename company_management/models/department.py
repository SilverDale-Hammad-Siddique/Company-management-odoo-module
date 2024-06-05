from odoo import api, fields, models


class Department(models.Model):
    _description = 'Departments'
    _name = 'department'

    name = fields.Char(string="Name")
    manager_id = fields.Many2one('res.users', string="Manager")
    employee_idd = fields.One2many('hr.employee', 'department_idd', string="Employees")
    parent_id = fields.Many2one('department', string="Parent Department")
    company_idd = fields.Many2one('company', string="Company")
    active = fields.Boolean(string="Active", default=True)
    employee_count = fields.Integer(string="Employees", compute='_compute_employee_count', readonly=True)
    total_employee = fields.Integer(string='Total Employee', compute='_compute_total_employee')
    color = fields.Integer(string='Color')
    label_employee = fields.Char(string="Label For Employees", default="Employees", tracking=True)

    @api.depends('employee_idd')
    def _compute_employee_count(self):
        for record in self:
            record.employee_count = len(record.employee_idd)

    @api.depends('employee_idd')
    def _compute_total_employee(self):
        for department in self:
            department.total_employee = len(department.employee_idd)


