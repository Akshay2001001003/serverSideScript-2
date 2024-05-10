frappe.ui.form.on("Dashboard", {
    refresh: function(frm) {
        // Make AJAX call to add_number_card_to_dashboard endpoint
        frappe.call({
            method: "customapp2.custom.dashboard.dashboard.add_number_card_to_dashboard",
            args: {
                dashboard_name: "cards",  // Provide the dashboard name
                title: "Customer Count",  // Provide the title for the number card
                value: 10,  // Replace with the actual count of customers
                unit: ""  // Provide the unit for the number card if any
            },
            callback: function(response) {
                // Handle response if needed
                console.log(response);
            }
        });
    }
});