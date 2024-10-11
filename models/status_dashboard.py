from odoo import models, fields

class StatusDashboard(models.Model):
    _name = 'status.dashboard'
    _description = 'Status Dashboard'

    name = fields.Char(string='Name', required=True)
    status = fields.Selection([
        ('online', 'Online'),
        ('partially', 'Partially'),
        ('offline', 'Offline'),
    ], string='Status', default='online')
    description = fields.Text(string='Description')
    reported_date = fields.Datetime(string='Reported Date', default=fields.Datetime.now)
    severity = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ], string='Severity', default='low', required=True)
    