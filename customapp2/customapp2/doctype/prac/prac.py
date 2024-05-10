# Copyright (c) 2024, me and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

# @frappe.whitelist(allow_guest=True)
# def getuser(doc):
#    response=frappe.get_doc("prac",doc)
#    return response

# @frappe.whitelist(allow_guest=True)
# def postuser(first_name,last_name,active,customer):
#    newuser=frappe.get_doc({
#       "doctype":"prac",
#       "first_name":first_name,
#       "last_name":last_name,
#       "active":active,
#       "customer":customer
#    })
#    newuser.insert()

# @frappe.whitelist(allow_guest=True)
# def updateuser(docname,first_name,last_name,active,customer):
#   frappe.db.set_value("prac",docname,"first_name",first_name)
#   frappe.db.set_value("prac",docname,"last_name",last_name)
#   frappe.db.set_value("prac",docname,"full_name",first_name+" "+last_name)
#   frappe.db.set_value("prac",docname,"active",active)
#   frappe.db.set_value("prac",docname,"customer",customer)

# @frappe.whitelist(allow_guest=True)
# def delete(docname):
#    frappe.db.delete("prac",docname)

@frappe.whitelist(allow_guest=True)
def getuser(doc):
    try:
        response = frappe.get_doc("prac", doc)
        return response
    except Exception as e:
        frappe.log_error(f"Error in getuser: {e}")
        frappe.response['http_status_code'] = 500
        return {"error": str(e)}

@frappe.whitelist()
def postuser(first_name, last_name, active, customer):
    try:
        newuser = frappe.get_doc({
            "doctype": "prac",
            "first_name": first_name,
            "last_name": last_name,
            "active": active,
            "customer": customer
        })
        newuser.insert()
        return {"message": "User created successfully"}
    except Exception as e:
        frappe.log_error(f"Error in postuser: {e}")
        frappe.response['http_status_code'] = 500
        return {"error": str(e)}

@frappe.whitelist(allow_guest=True)
def updateuser(docname, first_name, last_name, active, customer):
    try:
        frappe.db.set_value("prac", docname, "first_name", first_name)
        frappe.db.set_value("prac", docname, "last_name", last_name)
        frappe.db.set_value("prac", docname, "full_name", first_name + " " + last_name)
        frappe.db.set_value("prac", docname, "active", active)
        frappe.db.set_value("prac", docname, "customer", customer)
        return {"message": "User updated successfully"}
    except Exception as e:
        frappe.log_error(f"Error in updateuser: {e}")
        frappe.response['http_status_code'] = 500
        return {"error": str(e)}

@frappe.whitelist(allow_guest=True)
def delete(docname):
    try:
        if not frappe.get_doc("prac", docname):
            return {"message":f"user not found"}
        frappe.db.delete("prac", docname)
        return {"message": f"User {docname} deleted successfully"}
    except Exception as e:
        frappe.log_error(f"Error in delete: {e}")
        frappe.response['http_status_code'] = 500
        return {"error": str(e)}

class prac(Document):
	
    @frappe.whitelist()
    def validate(self):
      if(self.active==1):
         self.full_name=f'{self.first_name} {self.last_name}'
    
         customer=frappe.get_doc("Customer",self.customer)
    #    frappe.throw(str(customer))
         self.customer_group=customer.customer_group
         self.account_manager=customer.account_manager
         self.billing_currency=customer.default_currency
         self.default_price_list=customer.default_price_list
       