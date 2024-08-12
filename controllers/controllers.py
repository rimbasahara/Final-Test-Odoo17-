# -*- coding: utf-8 -*-
# from odoo import http


# class OdooBooklibrary(http.Controller):
#     @http.route('/odoo_booklibrary/odoo_booklibrary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_booklibrary/odoo_booklibrary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_booklibrary.listing', {
#             'root': '/odoo_booklibrary/odoo_booklibrary',
#             'objects': http.request.env['odoo_booklibrary.odoo_booklibrary'].search([]),
#         })

#     @http.route('/odoo_booklibrary/odoo_booklibrary/objects/<model("odoo_booklibrary.odoo_booklibrary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_booklibrary.object', {
#             'object': obj
#         })

