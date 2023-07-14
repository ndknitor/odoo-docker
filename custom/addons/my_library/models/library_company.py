from odoo import models, fields


class LibraryCompany(models.Model):
    _name = 'library.company'
    _description = 'Company'

    name = fields.Char('Name')
    company_phone_number = fields.Char('Company phone no.')
    description = fields.Text('Description')
