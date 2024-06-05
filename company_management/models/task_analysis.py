from odoo import models, fields, api


class TaskAnalysis(models.Model):
    _description = 'Reports'
    _name = 'report.task'

    project_idd = fields.Many2one('project', string='Project')
    nbr = fields.Integer(string='Number')
    # stage_id = fields.Many2one('project.task.stage', string='Stage')

    @api.depends('project_idd')
    def _compute_project_tasks_count(self):
        for record in self:
            tasks_count = self.env['project.task'].search_count([('project_id', '=', record.project_idd.id)])
            record.tasks_count = tasks_count

    tasks_count = fields.Integer(string='Tasks Count', compute='_compute_project_tasks_count')

    def action_view_tasks(self):
        """Method to open tasks associated with the project."""
        action = self.env.ref('project.action_view_task').read()[0]
        action['domain'] = [('project_id', '=', self.project_idd.id)]
        return action
