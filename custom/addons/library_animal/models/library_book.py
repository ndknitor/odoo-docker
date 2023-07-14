# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _inherit = 'library.book'

    animal_line_ids = fields.One2many('library.book.line', 'book_id', string='Animals')
    country_line_ids = fields.One2many('library.book.line.people', 'book_id', string='Countries')


class LibraryBookLine(models.Model):
    _name = 'library.book.line'

    animal_id = fields.Many2one('library.animal', string='Animal')
    age = fields.Integer(string='Age')
    book_id = fields.Many2one('library.book')


class LibraryBookLinePeople(models.Model):
    _name = 'library.book.line.people'

    book_id = fields.Many2one('library.book')
    country_id = fields.Many2one('res.country', string='Country')
    country_count = fields.Integer(string='Count')

    _sql_constraints = [
        ('country_uniq', 'UNIQUE (country_id)', 'Country must be unique.')
    ]
