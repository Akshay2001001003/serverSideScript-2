import frappe
import plotly.graph_objects as go

@frappe.whitelist(allow_guest=True)
def get_data():
    # Get the count of customers
    data = frappe.get_all("prac", filters={"customer": ("!=", "")})
    count = len(data)
    
    # Create the number card
    card = go.Figure(go.Indicator(
        mode="number",
        value=count,
        title={"text": "Customer Count"},
        number={"suffix": ""}
    ))
    
    # Convert the card to JSON format
    card_json = card.to_json()
    
    # Return the card JSON representation along with the count
    return {"count": count, "card": card_json}
