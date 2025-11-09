/* @odoo-module */

import { Component } from "@odoo/owl";
import { registry } from  "@web/core/registry";

export class ListViewAction extends Component {
    // Component logic goes here

    static template = "app_one.ListView";
}

registry.category("actions").add("app_one.list_view_action", ListViewAction);
