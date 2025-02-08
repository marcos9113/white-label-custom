/** @odoo-module **/
/*  Copyright 2015-2018,2022-2023 Ivan Yelizariev <https://twitter.com/yelizariev>
    Copyright 2017 ArtyomLosev <https://github.com/ArtyomLosev>
    Copyright 2022 IT-Projects <https://it-projects.info/>
    License MIT (https://opensource.org/licenses/MIT). */

import { debrandTranslation } from "@gamerun_whitelabel/js/translation";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { WebClient } from "@web/webclient/webclient";

const { onMounted } = owl;
const components = { WebClient };

patch(components.WebClient.prototype, {
    setup() {
        super.setup();
        odoo.debranding_new_name = "";
        odoo.debranding_new_website = "";
        odoo.debranding_new_title = "";
        this.title.setParts({ zopenerp: odoo.debranding_new_title });
        this.orm = useService("orm");
        onMounted(() => {
            this.updateDebrandingValues();
        });
    },
    async updateDebrandingValues() {
        const result = await this.orm.call(
            "ir.config_parameter",
            "get_debranding_parameters"
        );
        odoo.debranding_new_name = result["gamerun_whitelabel.new_name"];
        odoo.debranding_new_website = result["gamerun_whitelabel.new_website"];
        odoo.debranding_new_title = result["gamerun_whitelabel.new_title"];
        this.title.setParts({ zopenerp: odoo.debranding_new_title });
        debrandTranslation();
    },
});
