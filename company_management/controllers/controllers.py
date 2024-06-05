from io import BytesIO
import xlsxwriter
from odoo.http import request, Response
from odoo import http


class EmployeeReport(http.Controller):
    @http.route('/employee/report', type='http', auth='user')
    def get_employee_report(self, employee_ids=None, row_height=20, col_width=20, **kwargs):
        if employee_ids:
            employee_ids = list(map(int, employee_ids.split(',')))
            employee_records = request.env['hr.employee'].browse(employee_ids)
        else:
            employee_records = request.env['hr.employee'].search([])

        output = BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Employee Report')
        bold = workbook.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter'})  # Format for centered text
        centered = workbook.add_format({'align': 'center', 'valign': 'vcenter'})  # New format for centered text
        headers = [
            'Employee ID',
            'Name',
            'Phone',
            'Department',
            'Company',
            'Active',
            'My Employee'
        ]
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header, bold)
            worksheet.set_column(col_num, col_num, col_width)

        row_num = 1  # Initialize row_num outside the loop

        for record in employee_records:
            worksheet.write(row_num, 0, record.id, centered)
            worksheet.write(row_num, 1, record.name, centered)
            worksheet.write(row_num, 2, record.phone, centered)
            worksheet.write(row_num, 3, record.department_idd.name if record.department_idd else '', centered)
            worksheet.write(row_num, 4, record.company_idd.name if record.company_idd else '', centered)
            worksheet.write(row_num, 5, record.active, centered)
            worksheet.write(row_num, 6, record.my_employee, centered)
            worksheet.set_row(row_num, row_height)
            row_num += 1

        workbook.close()
        output.seek(0)
        file_data = output.read()
        output.close()
        response = request.make_response(
            file_data,
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename=Employee_Report.xlsx;')
            ]
        )
        return response
