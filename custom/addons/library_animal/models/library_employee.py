from odoo import models, fields


class LibraryEmployee(models.Model):
    _name = 'library.employee'
    _description = 'Employee'

    name = fields.Char('Name')
    phone_number = fields.Char('Phone Number')
    photo = fields.Binary(string="Photo")
    description = fields.Text('Description')
    age = fields.Integer('Age')
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female')],
        'Gender', default='male')


class LibraryCompanyEmployee(models.Model):
    _inherit = 'library.company'

    employee_ids = fields.One2many('library.company.line', 'company_id', string='Employees')


class LibraryCompanyLine(models.Model):
    _name = 'library.company.line'

    company_id = fields.Many2one('library.company')
    employee_id = fields.Many2one('library.employee', string='Employee')
    position = fields.Char('Position')
