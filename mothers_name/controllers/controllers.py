# -*- coding: utf-8 -*-
# from odoo import http


# class MothersName(http.Controller):
#     @http.route('/mothers_name/mothers_name/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mothers_name/mothers_name/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mothers_name.listing', {
#             'root': '/mothers_name/mothers_name',
#             'objects': http.request.env['mothers_name.mothers_name'].search([]),
#         })

#     @http.route('/mothers_name/mothers_name/objects/<model("mothers_name.mothers_name"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mothers_name.object', {
#             'object': obj
#         })
