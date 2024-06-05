from odoo import api, fields, models


class Project(models.Model):
    _description = 'Projects'
    _name = 'project'
    _inherit = ['mail.activity.mixin', 'mail.thread']

    name = fields.Char()
    display_name = fields.Char(string="Display Name")
    task_ids2 = fields.One2many('task', 'project_idd', string="Task")
    partner_id = fields.Many2one('res.partner', string="Customer", tracking=True)
    commercial_partner_id = fields.Many2one('res.partner', string="Commercial Partner")
    color = fields.Integer(string="Color")
    task_count = fields.Integer(string="Task Count", compute='_compute_task_count')
    description = fields.Html(string="Description")
    access_instruction_message = fields.Text(string="Access Instruction Message")
    message_follower_ids = fields.Many2many('hr.employee', 'project_idd', 'partner_id', string='Followers',
                                            tracking=True)
    milestone_count_reached = fields.Integer(string="Milestone Count Reached")
    date_start = fields.Date(string="Start Date", tracking=True)
    date_end = fields.Date(string="Start Date", tracking=True)
    employee_idd = fields.Many2one('hr.employee', tracking=True)
    milestone_count = fields.Integer(string="Milestone Count")
    rating_avg_percentage = fields.Float(string="Rating Average Percentage")
    allow_milestones = fields.Boolean(string="Allow Milestones")
    label_tasks = fields.Char(string="Label Tasks", default="Tasks", tracking=True)
    alias_name = fields.Char(string="Alias Name")
    alias_domain = fields.Char(string="Alias Domain")
    is_favorite = fields.Boolean(string="Is Favorite")
    rating_count = fields.Integer(string="Rating Count")
    sequence = fields.Integer(string="Sequence")
    active = fields.Boolean(string='Active', default=True)
    rating_avg = fields.Float(string="Rating Average")
    rating_status = fields.Char(string="Rating Status")
    company_idd = fields.Many2one('company', string='Company')
    rating_active = fields.Boolean(string="Rating Active")
    date = fields.Date(string="Date")

    privacy_visibility = fields.Selection([
        ('public', 'Invited internal users'),
        ('private', 'All internal users'),
        ('portal', 'Invited portal users and all internal users')],
        string="Privacy Visibility")
    last_update_color = fields.Integer(string="Last Update Color")
    last_update_status = fields.Char(string="Last Update Status")

    def _get_share_url(self, redirect=True):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        if redirect:
            return f'{base_url}/project/{self.id}/share/redirect'
        else:
            return f'{base_url}/project/{self.id}/share'

    def get_tasks_by_project(self, project_ids):
        domain = [('project_idd', 'in', project_ids)]
        tasks = self.env['task'].search(domain)
        return tasks

    def action_view_project_tasks(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tasks',
            'view_mode': 'tree,form,kanban,graph',
            'res_model': 'task',
            'domain': [('project_idd', '=', self.id)],
            'context': dict(self._context),
        }

    @api.model
    def _register_hook(self):
        self.env['ir.actions.act_window'].sudo().create({
            'name': 'View Tasks',
            'type': 'ir.actions.act_window',
            'res_model': 'task',
            'view_mode': 'tree,form,kanban,graph',
            'target': 'current',
            'context': "{'default_project_idd': active_id}",
        })
        return super(Project, self)._register_hook()

    @api.depends('task_ids2')
    def _compute_task_count(self):
        for record in self:
            record.task_count = len(record.task_ids2)
