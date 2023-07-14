# -*- coding: utf-8 -*-
from odoo import models, fields


class TestCompany(models.Model):
    _name = 'test.company'
    _description = 'Company manage'

    name = fields.Char('Company', required=True)
    employee_ids = fields.One2many('test.employee','tcompany_id', string = 'Employees')

