import frappe

@frappe.whitelist()
def export_customers():
    return frappe.db.sql(''' select cus.name,cus.customer_name,cus.email_id,cus.mobile_no,addr.address_line1,
                        addr.address_line2,addr.pincode,addr.city,addr.state,addr.country
                        from `tabCustomer` cus
                        left join `tabAddress` addr
                        on addr.name = cus.customer_primary_address
              ''',as_list=1)