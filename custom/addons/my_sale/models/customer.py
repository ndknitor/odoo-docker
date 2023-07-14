# -*- coding: utf-8 -*-
from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    rating_no = fields.Selection([
        ('1', 'Very Good'),
        ('2', 'Good'),
        ('3', 'So So'),
        ('4', 'Bad'),
    ],string = 'Customer rating')
