
frappe.listview_settings['Customer'] = {


    onload(listview) {
        listview.page.add_button('Export', () => {
            frappe.call({
                method: "customapp2.custom.query.export_customers",
                callback: result => {
                    if (result.message) {
                        let export_fields = [["Customer Name", "Customer Type", "Email id", "Mobile number", "Address Line1", "Address Line 2", "Pincode", "City", "State", "Country"]]
                        result.message.map(e => export_fields.push(e))
                        // frappe.message("done");
                        frappe.tools.downloadify(export_fields, null, 'Customer');
                    }
                    else{
                        // frappe.message("unable to print");
                        console.log("unable"+result.message);
                    }
                }
            })
        })
    }}