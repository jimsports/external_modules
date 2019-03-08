# -*- coding: utf-8 -*-
# © 2018 Comunitea - Kiko Sánchez <kiko@comunitea.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Stock Picking Group',
    'summary': 'Add grouped picks',
    'version': '11.0.1.0.0',
    'category': 'warehouse',
    'website': 'comunitea.com',
    'author': 'Comunitea',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'depends': [
        'sale_stock',
        'stock_picking_imp',
        'stock_move_manage'
    ],
    'data': [
        'views/sale_view.xml',
        'views/stock_move.xml',
        'views/stock_picking.xml',
        'views/stock_location.xml'
    ],
}