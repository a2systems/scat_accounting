from odoo import tools,fields, models, api, _

class AccountMove(models.Model):
    _inherit = "account.move"

    folio_interno = fields.Char("Folio Interno")
    folio_fiscal = fields.Char("Folio Fiscal")
    rfc = fields.Char("RFC")
    
