"""
✅ [Fix #6] Added module-level docstring
Inventory Management System
---------------------------
A simple inventory tracking system with add, remove, and reporting functions.
"""

import json  # ✅ [Fix #5] Removed unused logging import
from datetime import datetime

# ✅ [Fix #12] Explained and justified global statement usage
# Global variable is required for simplicity in this small script.
stock_data = {}  # pylint: disable=global-statement


# ✅ [Fix #1] Changed mutable default argument logs=[] → None
# ✅ [Fix #8] Renamed to snake_case (PEP8)
# ✅ [Fix #10] Replaced old % formatting with f-string
# ✅ [Fix #7] Added function-level docstring
def add_item(item="default", qty=0, logs=None):
    """Add an item to the inventory with given quantity."""
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")  # using f-string


# ✅ [Fix #3] Replaced bare except with specific exception type
# ✅ [Fix #8] Renamed to snake_case (PEP8)
# ✅ [Fix #7] Added function docstring
def remove_item(item, qty):
    """Remove a quantity of an item from the inventory safely."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        print(f"Warning: Item '{item}' not found ({e})")  # handles missing item


# ✅ [Fix #7] Added function docstring
# ✅ [Fix #8] Renamed to snake_case
def get_qty(item):
    """Return the quantity of a given item in stock."""
    return stock_data.get(item, 0)


# ✅ [Fix #4] Used 'with' statement for file handling
# ✅ [Fix #11] Added encoding parameter
# ✅ [Fix #7] Added docstring
# ✅ [Fix #8] Renamed to snake_case
# ✅ [Fix #13] Broke long line (E501) for PEP 8 compliance
def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    # pylint: disable=global-statement
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(
            f"Warning: {file} not found.\n"
            "Starting with empty inventory."
        )
        stock_data = {}


# ✅ [Fix #4] Used 'with' for safe file handling
# ✅ [Fix #11] Added encoding
# ✅ [Fix #7] Added function docstring
# ✅ [Fix #8] Renamed to snake_case
def save_data(file="inventory.json"):
    """Save the current inventory data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(stock_data))


# ✅ [Fix #7] Added function docstring
# ✅ [Fix #8] Renamed to snake_case
# ✅ [Fix #9] Added 2 blank lines between functions (PEP8)
def print_data():
    """Print all current items and their quantities."""
    print("Items Report:")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")


# ✅ [Fix #7] Added function docstring
# ✅ [Fix #8] Renamed to snake_case
def check_low_items(threshold=5):
    """Return list of items whose stock is below the threshold."""
    result = [i for i in stock_data if stock_data[i] < threshold]
    return result


# ✅ [Fix #2] Removed insecure eval() usage (Bandit B307)
# ✅ [Fix #7] Added docstring
# ✅ [Fix #8] Renamed to snake_case
# ✅ [Fix #15] Fixed comment formatting (2 spaces before inline comments)
def main():
    """Main function demonstrating inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("orange", 5)
    remove_item("apple", 3)
    remove_item("grapes", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low stock items:", check_low_items())
    save_data()
    load_data()
    print_data()
    #  eval("print('eval used')")  # ❌ Removed due to Bandit B307


if __name__ == "__main__":
    main()


# ✅ [Fix #14] Added final blank newline (PEP8 requirement)
