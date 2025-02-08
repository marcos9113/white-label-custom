/** @odoo-module **/

import "@web/webclient/user_menu/user_menu_items";
import { registry } from "@web/core/registry";

const menuItems = registry.category("user_menuitems");
menuItems.remove("documentation");
menuItems.remove("support");
menuItems.remove("shortcuts");
menuItems.remove("web_tour.tour_enabled");
menuItems.remove("separator");
menuItems.remove("install_pwa");
menuItems.remove("odoo_account");
