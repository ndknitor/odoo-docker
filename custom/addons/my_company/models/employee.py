# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TestEmployee(models.Model):
    _name = 'test.employee'

    name = fields.Char('Employee', required=True)
    tcompany_id = fields.Many2one('test.company', string = 'Company')
