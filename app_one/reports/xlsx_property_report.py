from ast import literal_eval
from odoo import http
from odoo.http import request
import io
import xlsxwriter



class PropertyReportXLSX(http.Controller):
    @http.route('/property/report/xlsx/<string:property_id>', type='http', auth='user')
    def generate_property_report_xlsx(self, property_id):
        
        #print ("Generating XLSX report for property ID:", property_id)

        property_ids = literal_eval(property_id) # Convert string representation of list back to list
        property_record = request.env['property'].browse(property_ids)

        if not property_record:
            return request.not_found()
        
        output = io.BytesIO() # Create an in-memory output file for the new workbook.
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Properties')

        # Define formats
        header_format = workbook.add_format({'bold': True, 'bg_color': '#D7E4BC', 'border': 1, 'align': 'center'})
        string_format = workbook.add_format({'border': 1, 'align': 'center'})
        price_format = workbook.add_format({'num_format': '$#,##0.00', 'border': 1, 'align': 'center'})
        headers =['Name', 'Postcode', 'Garden', 'State','Price']

        # Write headers
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header, header_format)

        # Write property lines
        row = 1
        for property in property_record:
            worksheet.write(row, 0, property.name, string_format)
            worksheet.write(row, 1, property.postcode, string_format)
            garden_value = "Yes" if property.garden else "No"
            worksheet.write(row, 2, garden_value, string_format)
            worksheet.write(row, 4, property.state, string_format)
            worksheet.write(row, 5, property.sold_price, price_format)
            row += 1

        workbook.close()
        output.seek(0) # Rewind the buffer to read the file from the beginning

        filename = 'Property_Report.xlsx'
        #filename = f'Property_Report.xlsx'

        return request.make_response(
            output.read(),
            #output.getvalue(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', f'attachment; filename="{filename}"')
            ]
        )