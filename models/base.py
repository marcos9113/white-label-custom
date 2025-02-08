from odoo import api, models

from .ir_translation import debrand

BRANDED_FIELDS = {}


class Base(models.AbstractModel):

    _inherit = "base"

    @api.model
    def search(self, domain, offset=0, limit=None, order=None):
        res = super().search(domain, offset, limit, order)
        if self._name == "payment.provider":
            res = res.filtered(lambda a: not a.module_to_buy)
        return res

    def get_view(self, view_id=None, view_type="form", **options):
        res = super().get_view(view_id=view_id, view_type=view_type, **options)
        res["arch"] = debrand(self.env, res["arch"], is_code=True)
        return res
