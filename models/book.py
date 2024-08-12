from odoo import models, fields, api

class Book(models.Model):
    _name = 'book.list'
    _description = 'Daftar Buku'

    judul = fields.Char(String = 'Judul', required=True)
    category = fields.Selection([
        ('umum', 'Umum'), 
        ('it', 'IT'), 
        ('kesehatan', 'Kesehatan'),
        ('politik', 'Politik')
        ], 
        String = 'Kategori', required = True, help = 'Pilih Kategori Buku')
    tanggal_terbit = fields.Date(String='Tanggal Terbit')
    penulis_ids = fields.Many2one('res.partner', String='Penulis')
    kode_isbn = fields.Char(String='Kode ISBN', required=True, unique=True)

    serial_number = fields.Char(string='Serial Number' )
    lokasi_buku = fields.Char(string='Lokasi Buku')
    qty_tersedia = fields.Integer(string='Qty Tersedia')

    ref = fields.Char(string='Referensi', readonly=True, default='-')
 
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('book.list')
        return super(Book, self).create(vals)