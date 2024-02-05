# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryAnimal(models.Model):
    _name = 'library.animal'
    _description = 'Library Animal'
    _order = 'name'

    name = fields.Char('Title', required=True, index=True)
    description = fields.Html('Description', sanitize=True, strip_style=False)


