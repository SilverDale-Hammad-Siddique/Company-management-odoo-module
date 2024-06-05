from odoo import models, fields, api


class ProjectTask(models.Model):
    _name = 'task'
    _inherit = ['mail.activity.mixin', 'mail.thread']

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Html(string='Description', tracking=True)
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal')])

    state = fields.Selection(
        selection=[
            ('new', 'NEW'),
            ('planing', 'PLANING'),
            ('in_progress', 'IN PROGRESS'),
            ('cancel', 'CANCEL'),
            ('done', 'DONE'), ], string='Status', default='inbox', tracking=True
    )
    message_follower_ids = fields.Many2many('hr.employee', 'task_idd', 'partner_id', string='Followers',
                                            tracking=True)
    employee_ids = fields.Many2many('hr.employee', string='Assignees', tracking=True)
    employee_idd = fields.Many2one('hr.employee', string='Employee')
    project_idd = fields.Many2one('project', string="Project", tracking=True)
    sequence = fields.Integer(string='Sequence', default=10, tracking=True)
    assign_date = fields.Date(string='Assign Date', tracking=True)
    date_deadline = fields.Datetime(string='Deadline', tracking=True)
    tags_idd = fields.Many2many('task.tag', string='Tags', tracking=True)
    last_stage_update = fields.Datetime(string='Last Stage Update', tracking=True)
    display_project_idd = fields.Many2one('project', string="Display Project", tracking=True)
    partner_idd = fields.Many2one('res.partner', string="Customer", tracking=True)
    timesheet_ids2 = fields.One2many('time.sheet.employee', 'task_idd', tracking=True)
    allocated_hours = fields.Float(string="Allocated Hours", widget="timesheet_uom_no_toggle", tracking=True)
    unit_amount = fields.Float(string="Hours Spent")
    color = fields.Char(string='Color')
    allow_milestones = fields.Boolean(string='Allow Milestones')
    planned_hours = fields.Float(string='Planned Hours', tracking=True)
    working_hours_open = fields.Float(string='Working Hours Open', widget="float_time",
                                      tracking=True)
    working_hours_close = fields.Float(string='Working Hours Close', widget="float_time",
                                       tracking=True)
    remaining_hours = fields.Float(string="Remaining Hours", compute="_compute_remaining_hours", store=True,
                                   tracking=True)
    progress = fields.Integer(string="Progress", compute='compute_progress')

    @api.depends('timesheet_ids2.unit_amount')
    def compute_progress(self):
        for rec in self:
            unit_amount_sum = sum(rec.timesheet_ids2.mapped('unit_amount'))
            if unit_amount_sum <= 0:
                progress = 0
            elif unit_amount_sum <= 1:
                progress = 15
            elif unit_amount_sum <= 2:
                progress = 25
            elif unit_amount_sum <= 3:
                progress = 35
            elif unit_amount_sum <= 4:
                progress = 50
            elif unit_amount_sum <= 5:
                progress = 70
            elif unit_amount_sum <= 6:
                progress = 85
            elif unit_amount_sum <= 7:
                progress = 95
            else:
                progress = 100  # If more than 5 hours, consider task complete

            rec.progress = progress

    @api.depends('allocated_hours', 'unit_amount')
    def _compute_remaining_hours(self):
        for record in self:
            remaining_hours = record.allocated_hours - record.unit_amount
            record.remaining_hours = max(0, remaining_hours)

    @api.onchange('unit_amount')
    def _onchange_unit_amount(self):
        for record in self:
            record.remaining_hours = max(0, record.allocated_hours - record.unit_amount)

    def action_assign_to_me(self):
        # Here you can add your logic for assigning the task to the current user
        # For example, if you have a field named 'assigned_to' representing the assigned user:
        for task in self:
            task.write({'assigned_to': self.env.user.id})
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
