# my_custom_app/my_custom_app/report/sales_order_report.py

import frappe

def execute(filters=None):
    columns = [
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Link", "options": "Customer"},
        {"label": "Sales Order", "fieldname": "sales_order", "fieldtype": "Link", "options": "Sales Order"},
        {"label": "Delivery Date", "fieldname": "delivery_date", "fieldtype": "Date"},
        {"label": "Item Code", "fieldname": "item_code", "fieldtype": "Link", "options": "Item"},
        {"label": "Item Name", "fieldname": "item_name", "fieldtype": "Data"},
        {"label": "Item Quantity", "fieldname": "item_qty", "fieldtype": "Float"}
    ]

    data = []

    # Fetch data from Sales Order doctype
    sales_orders = frappe.get_all("Sales Order", filters=filters, fields=["name", "customer", "delivery_date"])
    for so in sales_orders:
        items = frappe.get_all("Sales Order Item", filters={"parent": so.name}, fields=["item_code", "item_name", "qty"])
        for item in items:
            data.append({
                "customer_name": so.customer,
                "sales_order": so.name,
                "delivery_date": so.delivery_date,
                "item_code": item.item_code,
                "item_name": item.item_name,
                "item_qty": item.qty
            })

    return columns, data
