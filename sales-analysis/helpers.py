# helpers.py

def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity * price
# Function to format currency
def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}"