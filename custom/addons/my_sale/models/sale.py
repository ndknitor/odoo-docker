# -*- coding: utf-8 -*-
from odoo import models, fields ,api
import logging
_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    rating_no = fields.Selection(related='partner_id.rating_no',string = 'Customer rating')


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """

        for line in self:

            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
                                            product=line.product_id, partner=line.order_id.partner_shipping_id)
            price_subtotal = taxes['total_excluded']

            if line.order_id.rating_no == '1':
               price_subtotal = price_subtotal - price_subtotal*0.3
            elif  line.order_id.rating_no == '2':
               price_subtotal = price_subtotal - price_subtotal*0.1

            _logger.warning('--rating_no %s price_subtotal %s',line.order_id.rating_no, price_subtotal)

            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': price_subtotal,
            })
