from odoo import models, fields


class Animal(models.Model):
    _name = 'animal'
    _description = 'Animal'

    name = fields.Char('Name', require=True)
    book_ids = fields.Many2one('library.book', string='Book')


class LibraryBook(models.Model):
    _inherit = 'library.book'

    animals = fields.One2many('animal', 'book_ids', string='Animals')
