# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryCountry(models.Model):
    _name = 'library.country'
    _description = 'Library Country'
    _order = 'name'

    name = fields.Char('Name', required=True, index=True)


