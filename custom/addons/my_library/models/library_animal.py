# -*- coding: utf-8 -*-
from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)

class LibraryAnimal(models.Model):
    _name = 'library.animal'
    _description = 'Library Animal'
    _order = 'name'

    name = fields.Char('Animal Name')
    age = fields.Integer('Age')

