from odoo import models, fields, api

class RentTransaction(models.Model):
    _name = 'rent.transaction'
    _description = 'Transaksi Rental'

    tanggal_rental = fields.Date(String='Tanggal Rental', required=True)
    nama_peminjam = fields.Many2one('library.member', String='Nama Peminjam', required=True)
    list_buku_id = fields.Many2one('book.list', string='List Buku')
    list_buku = fields.Char(related='list_buku_id.judul', string='Judul Buku', store=True)
    status_transaksi = fields.Selection([
        ('dipinjam', 'Sedang Dipinjam'),
        ('belum_dikembalikan', 'Belum Dikembalikan'),
        ('selesai', 'Selesai'),
    ], String='Status Transaksi', default='dipinjam')

class RentTransactionLine(models.Model):
    _name = 'rent.transaction.line'
    _description = 'List Transaksi Rental'

    book_id = fields.Many2one('book.list', string='Buku', required=True)
    lokasi_buku = fields.Char(related='book_id.lokasi_buku', string='Lokasi Buku', readonly=True)
    
    qty = fields.Integer(string='Jumlah Buku', required=True)
    transaction_id = fields.Many2one('rent.transaction', string='Transaction')
    tanggal_mulai = fields.Date(string='Tanggal Mulai', required=True)
    tanggal_selesai = fields.Date(string='Tanggal Selesai', required=True)
    total_biaya_sewa = fields.Float(string='Total Biaya Sewa')
    pengembalian = fields.Boolean(string='Pengembalian?', default=False)