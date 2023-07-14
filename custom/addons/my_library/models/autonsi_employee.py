from odoo import models, fields


class AutonsiEmployee(models.Model):
    _name = 'autonsi.employee'
    _description = 'Autonsi Employee'

    name = fields.Char('Name', require=True)
    employee_number = fields.Char('Employee Number')
    photo = fields.Binary(string="Photo")
    position = fields.Char('Position')
    description = fields.Text('Work Detail')
    age = fields.Integer('Age')
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female')],
        'Gender', default='female')

    _sql_constraints = [
        ('positive_age', 'CHECK(age>0)', 'Age must be positive')
    ]
