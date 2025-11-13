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
            bedrooms: 0,
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
                bedrooms: parseInt(this.state.bedrooms) || 0,
                expected_selling_date: this.state.expected_selling_date,
            }],
            kwargs: {},
        });
        if (this.props.onRecordCreated) {
            this.props.onRecordCreated();
        }
    }
    cancel() {
        this.state.name = "";
        this.state.description = "";
        this.state.postcode = "";
        this.state.bedrooms = 0;
        this.state.expected_selling_date = "";
        if (this.props.onCancel) {
            this.props.onCancel();
        }
    }

}