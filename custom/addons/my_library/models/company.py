from odoo import models, fields


class Company(models.Model):
    _name = 'company'
    _description = 'Company'

    name = fields.Char('Name')
    number = fields.Char('Number')
    description = fields.Text('Description')
