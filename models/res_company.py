from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    def _get_default_favicon(self, original=False):
        return None

    favicon = fields.Binary(default=_get_default_favicon)
