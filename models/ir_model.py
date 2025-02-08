from odoo import models

from .ir_translation import debrand


class IrModelSelection(models.Model):
    _inherit = "ir.model.fields.selection"

    def _get_selection_data(self, *args, **kwargs):
        data = super(IrModelSelection, self)._get_selection_data(*args, **kwargs)
        return [(value, debrand(self.env, name)) for value, name in data]
