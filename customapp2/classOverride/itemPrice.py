import frappe
from frappe.model.document import Document

class ItemPrice(Document):
    def validate(self):
        frappe.msgprint( "This class is overrided" )