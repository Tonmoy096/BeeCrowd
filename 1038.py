# Price table
prices = {
    1: 4.00,
    2: 4.50,
    3: 5.00,
    4: 2.00,
    5: 1.50
}

# Input: Product code (X) and quantity (Y)
X, Y = map(int, input().split())

# Calculate total
total = prices[X] * Y

# Output result
print(f"Total: R$ {total:.2f}")
