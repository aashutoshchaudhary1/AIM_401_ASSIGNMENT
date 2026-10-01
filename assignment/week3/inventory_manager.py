# ---------------------------------------------------------------
# Lesson 3 Individual Assignment: In-Memory Inventory Manager
# Distribution center order-processing script
# Uses only: lists, dictionaries, tuples, string formatting,
# if-elif-else, loops, and .get() / .append() / .items()
# ---------------------------------------------------------------

# ---------- TASK 1: Data setup ----------
# Inventory: item name -> units currently in stock
inventory = {
    "Widget": 10,
    "Gadget": 5,
    "Sensor": 0,
    "Cable": 15,
    "Battery": 20
}

# Order queue: each sub-list is [item name, requested quantity]
orders = [
    ["Widget", 3],     # full fulfillment
    ["Sensor", 2],     # out of stock
    ["Gadget", 7],     # partial fulfillment (only 5 available)
    ["Cable", 10],     # full fulfillment
    ["Bolt", 4],       # item does not exist in inventory
    ["Widget", 9],     # partial fulfillment (only 7 left)
    ["Cable", 5],      # full fulfillment (empties the stock)
    ["Cable", 1],      # out of stock (just emptied by previous order)
    ["Battery", 6]     # full fulfillment
]

# Analytics trackers
fully_fulfilled_count = 0
unfulfilled_items = []   # holds [item, quantity that could not be supplied]

# ---------- TASK 2: Order processing ----------
print("=" * 55)
print("PROCESSING ORDER BATCH")
print("=" * 55)

order_number = 1
for order in orders:
    item = order[0]
    requested = order[1]

    # .get() returns None when the key does not exist
    stock = inventory.get(item)

    print(f"Order #{order_number}: {requested} x {item}")

    if stock is None:
        # Invalid / missing item
        print(f"   ALERT: '{item}' does not exist in the inventory.")
        unfulfilled_items.append([item, requested])

    elif stock >= requested:
        # Full fulfillment
        inventory[item] = stock - requested
        fully_fulfilled_count += 1
        print(f"   SUCCESS: Fully fulfilled {requested} x {item}. "
              f"Remaining stock: {inventory[item]}")

    elif stock > 0:
        # Partial fulfillment: ship what is left, record the remainder
        remainder = requested - stock
        inventory[item] = 0
        unfulfilled_items.append([item, remainder])
        print(f"   PARTIAL: Shipped {stock} x {item}; "
              f"{remainder} unfulfilled. Stock is now 0.")

    else:
        # Stock is exactly 0
        print(f"   ALERT: '{item}' is OUT OF STOCK.")
        unfulfilled_items.append([item, requested])

    order_number += 1

# ---------- TASK 3: Summary report ----------
print()
print("=" * 55)
print("END-OF-BATCH SUMMARY REPORT")
print("=" * 55)

print("1. Final inventory:")
print("  ", inventory)
for name, count in inventory.items():
    print(f"   - {name:<8}: {count}")

print()
print(f"2. Total fully fulfilled orders: {fully_fulfilled_count} "
      f"of {len(orders)}")

print()
print("3. Items/quantities that could not be fully supplied:")
if len(unfulfilled_items) == 0:
    print("   None - every order was fully supplied.")
else:
    for entry in unfulfilled_items:
        print(f"   - {entry[0]}: {entry[1]} unit(s) short")
print("=" * 55)
