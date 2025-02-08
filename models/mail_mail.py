from odoo import models


class MailMail(models.AbstractModel):
    _inherit = "mail.mail"

    def _prepare_outgoing_body(self):
        body_html = super()._prepare_outgoing_body()

        # Use to_keep=None to force remove all Powered by Odoo texts
        # otherwise, use to_keep=self.body to keep what is in the body
        return self.env["mail.render.mixin"].remove_href_odoo(
            body_html or "", to_keep=None
        )
