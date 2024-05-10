import frappe
from plotly.graph_objs import Figure, Indicator

def add_number_card_to_dashboard(dashboard_name, title, value, unit):
    # Load the dashboard document
    dashboard = frappe.get_doc("Dashboard", dashboard_name)

    # Create a Plotly number card
    card = Figure(
        Indicator(
            mode="number",
            value=value,
            title={"text": title},
            number={"suffix": unit}
        )
    )

    # Add the Plotly card to the dashboard
    dashboard.cards.append({
        "type": "plotly",
        "width": "Half",
        "card_json": card.to_dict()
    })

    # Save the dashboard
    dashboard.save()

# Example usage:
dashboard_name = "cards"
title = "Customer Count"
value = 10  # Replace with the actual count of customers
unit = ""

add_number_card_to_dashboard(dashboard_name, title, value, unit)
