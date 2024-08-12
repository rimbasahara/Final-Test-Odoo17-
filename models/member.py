from odoo import models, fields, api

class Member(models.Model):
    _name = 'library.member'
    _description = 'Member'

    name = fields.Char(string='Nama', required=True)
    no_identitas = fields.Char(string='No Identitas', required=True, unique=True)
    jenis_kartu_identitas = fields.Selection([
        ('ktp', 'KTP'),
        ('sim', 'SIM'),
        ('pasport', 'Pasport'),
    ], string='Jenis Kartu Identitas', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    ], string='State', default='draft')
