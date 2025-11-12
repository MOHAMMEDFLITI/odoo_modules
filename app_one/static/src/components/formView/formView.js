/* @odoo-module */

import { Component, useState, onWillUnmount } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

export class FormView extends Component {

    static template = "app_one.FormView";
    setup() {
        this.state = useState({
            name: "",
            description: "",
            postcode: "",
            expected_selling_date: "",
        });



        onWillUnmount(() => {
        });
    }



    async createRecord() {
        await rpc("/web/dataset/call_kw/", {
            model: "property",
            method: "create",
            args: [{
                name: this.state.name,
                descreption: this.state.description,
                postcode: this.state.postcode,
                expected_selling_date: this.state.expected_selling_date,
            }],
            kwargs: {},
        });
    }
    cancel() {
        this.state.name = "";
        this.state.description = "";
        this.state.postcode = "";
        this.state.expected_selling_date = "";
    }

}