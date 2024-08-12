from odoo import models, fields

class BookManagement(models.Model):
    _name = 'book.management'
    _description = 'Manajemen Buku'

    book_id = fields.Many2one('book.list', string='Judul Buku', required=True)
    serial_number = fields.Char(string='Serial Number', required=True, unique=True)
    lokasi_buku = fields.Char(string='Lokasi Buku')
    qty_tersedia = fields.Integer(string='Qty Tersedia')
