{
    'name': "Company Management",
    'summary': "Company Management",
    'description': "Company Management",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'hr',


    ],
    'data': [
        'security/ir.model.access.csv',
        'demo/demo.xml',
        'views/company_view.xml',
        'views/contact_view.xml',
        'views/employee_view.xml',
        'views/employee2_view.xml',
        'views/department_view.xml',
        'views/menu.xml',
        'views/project_view.xml',
        'views/project2_view.xml',
        'views/res_config_settings_views.xml',
        'views/task_analysis_view.xml',
        'views/task_view.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/activity_view.xml',
        'views/task_tag_view.xml',
        'views/timesheet_view.xml',
        'views/report_employee.xml',
        'report/report_action.xml',
    ],
    'sequence': -10,
    'application': True,
}