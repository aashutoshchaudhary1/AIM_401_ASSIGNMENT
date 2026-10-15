"""
AIM 401: Python Programming for Data Science
Lesson 4 Individual Assignment
Functional Audit Tool for a Digital Banking System

Author: Aashutosh
Institution: International American University (IAU)

Task 1: clean_transactions() and apply_service_fee() use filter()/map() with lambdas.
Task 2: calculate_nested_total() is purely recursive (no loops, no global state).
"""


def clean_transactions(amounts, min_threshold=10.0):
    """Keep only transactions that are positive and at least min_threshold."""
    return list(filter(lambda amount: amount > 0 and amount >= min_threshold, amounts))


def apply_service_fee(amounts, fee_rate=0.02):
    """Deduct a percentage service fee from every amount (rounded to 2 decimals)."""
    return list(map(lambda amount: round(amount * (1 - fee_rate), 2), amounts))


def calculate_nested_total(data):
    """Recursively total a number or an arbitrarily nested list of numbers."""
    # Base case 1: empty list contributes nothing
    if isinstance(data, list) and len(data) == 0:
        return 0.0
    # Base case 2: a single numeric value
    if isinstance(data, (int, float)):
        return data
    # Recursive step: split into head and tail, resolve both, and add
    head = data[0]
    tail = data[1:]
    return calculate_nested_total(head) + calculate_nested_total(tail)


def main():
    raw_batch = [120.0, -15.5, 250.0, 0, 8.75, 42.5, 9.99, 1000.0, 75.0, 10.0]
    nested_batch = [100, [50, 25], [[10, 5], 40]]

    print("=" * 52)
    print("  DIGITAL BANKING AUDIT TOOL")
    print("=" * 52)

    print("\n--- Task 1: Functional Tools ---")
    print("Raw batch        :", raw_batch)
    cleaned = clean_transactions(raw_batch)
    print("Cleaned (>= 10.0):", cleaned)
    processed = apply_service_fee(cleaned)
    print("After 2% fee     :", processed)
    print("After 1% fee     :", apply_service_fee(cleaned, fee_rate=0.01))

    print("\n--- Task 2: Recursive Nested Total ---")
    print("Nested batch     :", nested_batch)
    print("Nested total     :", calculate_nested_total(nested_batch))

    print("\n--- Base Case and Edge Case Tests ---")
    print("[]                      ->", calculate_nested_total([]))
    print("42                      ->", calculate_nested_total(42))
    print("[1.0]                   ->", calculate_nested_total([1.0]))
    print("[[[1.0, 2.0], 3.0], 4.0] ->", calculate_nested_total([[[1.0, 2.0], 3.0], 4.0]))
    print("[[], [[]], 5]           ->", calculate_nested_total([[], [[]], 5]))


if __name__ == "__main__":
    main()
