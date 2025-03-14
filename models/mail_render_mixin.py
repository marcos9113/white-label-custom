import re

from lxml import etree, html
from markupsafe import Markup

from odoo import api, models


class MailRenderMixin(models.AbstractModel):
    _inherit = "mail.render.mixin"

    def remove_href_odoo(self, value, to_keep=None):
        if len(value) < 20:
            return value
        # value can be bytes or markup; ensure we get a proper string and preserve type
        back_to_bytes = False
        back_to_markup = False
        if isinstance(value, bytes):
            back_to_bytes = True
            value = value.decode()
        if isinstance(value, Markup):
            back_to_markup = True
        has_dev_odoo_link = re.search(
            r"<a\s(.*)dev\.odoo\.com", value, flags=re.IGNORECASE
        )
        has_odoo_link = re.search(r"<a\s(.*)odoo\.com", value, flags=re.IGNORECASE)
        if has_odoo_link and not has_dev_odoo_link:
            # We don't want to change what was explicitly added in the message body,
            # so we will only change what is before and after it.
            if to_keep:
                value = value.replace(to_keep, "<body_msg></body_msg>")
            tree = html.fromstring(value)
            odoo_anchors = tree.xpath('//a[contains(@href,"odoo.com")]')
            for elem in odoo_anchors:
                parent = elem.getparent()
                # Remove "Powered by", "using" etc.
                previous = elem.getprevious()
                if previous is not None:
                    previous.tail = etree.CDATA("&nbsp;")
                elif parent.text:
                    parent.text = etree.CDATA("&nbsp;")
                parent.remove(elem)
            value = etree.tostring(
                tree, pretty_print=True, method="html", encoding="unicode"
            )
            if to_keep:
                value = value.replace("<body_msg></body_msg>", to_keep)
        if back_to_bytes:
            value = value.encode()
        elif back_to_markup:
            value = Markup(value)

        return value

    @api.model
    def _render_template(
            self,
            template_src,
            model,
            res_ids,
            engine="inline_template",
            add_context=None,
            options=None,
    ):
        """replace anything that is with odoo in templates
        if is a <a that contains odoo will delete it completely
        original:
         Render the given string on records designed by model / res_ids using
        the given rendering engine.

        :param str template_src: template text to render (jinja) or  (qweb)
          this could be cleaned but hey, we are in a rush
        :param str model: model name of records on which we want to perform rendering
        :param list res_ids: list of ids of records (all belonging to same model)
        :param string engine: inline_template, qweb or qweb_view;
        :param post_process: perform rendered str / html post processing (see
          ``_render_template_postprocess``)

        :return dict: {res_id: string of rendered template based on record}"""
        original_rendered = super()._render_template(
            template_src,
            model,
            res_ids,
            engine=engine,
            add_context=add_context,
            options=options,
        )

        for key in res_ids:
            original_rendered[key] = self.remove_href_odoo(original_rendered[key])

        return original_rendered
