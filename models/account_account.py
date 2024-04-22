from odoo import tools,fields, models, api, _

class AccountAccount(models.Model):
    _inherit = "account.account"

    codigo_mx = fields.Char("Código MX")
    
