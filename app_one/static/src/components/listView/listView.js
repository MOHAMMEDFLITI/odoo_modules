/* @odoo-module */

import { Component, useState, onWillUnmount } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { rpc } from "@web/core/network/rpc";

export class ListViewAction extends Component {
    // Component logic goes here

    static template = "app_one.ListView";
    setup() { // OWL lifecycle method
        // this.records = [ //  { id: 1, name: "Record One", description: "This is the first record.", postcode: "12345" },
        // ]
        this.state = useState({
            records: [],
        });
        // this.orm = useService("orm");

        //this.loadRecords();
        this.intervalId = setInterval(() => {
            this.loadRecords();
        }, 3000); // Refresh every 3 seconds
        
        onWillUnmount(() => {
            clearInterval(this.intervalId);
        });
    }

    // async loadRecords() {
    //     // Logic to load records from the backend or other sources
    //     const result = await this.orm.searchRead("property", [], ["name", "descreption", "postcode"]);
    //     console.log("Loaded records:", result);
    //     this.state.records = result;
    // }

    async loadRecords() {
        const result = await rpc("/web/dataset/call_kw/", {
            model: "property",
            method: "search_read",
            args: [[]],
            kwargs: { fields: ["id", "name", "descreption", "postcode"] },
        });
        console.log("Loaded records:", result);
        this.state.records = result;
    }
}

registry.category("actions").add("app_one.list_view_action", ListViewAction);
