/* @odoo-module */

import { Component, useState, onWillUnmount } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { rpc } from "@web/core/network/rpc";
import { FormView } from "@app_one/components/formView/formView";

export class ListViewAction extends Component {

    static template = "app_one.ListView";
    static components = { FormView };


    setup() { // OWL lifecycle method
        // this.records = [ //  { id: 1, name: "Record One", description: "This is the first record.", postcode: "12345" },
        // ]
        this.state = useState({
            records: [],
        });
        // this.orm = useService("orm");

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
            args: [[]], // No domain filter
            kwargs: { fields: ["id", "name", "descreption", "postcode"] }, // Fields to retrieve
        });
        console.log("Loaded records:", result);
        this.state.records = result;
    }
    // create record using orm

    //     async createRecord() {
    //     const newRecord = {
    //         name: "CC",
    //         descreption: "Description of CC",
    //         postcode: "5300",
    //         bedrooms: 5,
    //         expected_selling_date: "2025-11-30",
    //     };
    //     await this.orm.create("property", [newRecord]);
    //     this.loadRecords(); // Refresh the list after creating a new record
    // }

    // create record using rpc
    async createRecord() {
        const newRecord = {
            name: "CC",
            descreption: "Description of CC",
            postcode: "5300",
            bedrooms: 5,
            expected_selling_date: "2025-11-30",
        };
        await rpc("/web/dataset/call_kw/", {
            model: "property",
            method: "create",
            args: [newRecord],
            kwargs: {},
        });
        this.loadRecords(); // Refresh the list after creating a new record
    }

    async deleteRecord(recordId) {
        await rpc("/web/dataset/call_kw/", {
            model: "property",
            method: "unlink",
            args: [recordId],
            kwargs: {},
        });
        this.loadRecords(); // Refresh the list after deleting a record
    }

    toggleCreateForm() {
        this.state.showCreateForm = !this.state.showCreateForm;
        console.log("Create form toggled");
    }
}

registry.category("actions").add("app_one.list_view_action", ListViewAction);
