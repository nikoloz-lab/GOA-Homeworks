def arithmetic_operations(a, b, c):
    product = a * b * c
    division = a / b / c if b != 0 and c != 0 else "Cannot divide by zero."
    difference = a - b - c
    sum_ = a + b + c
    print(f"Product: {product}, Division: {division}, Difference: {difference}, Sum: {sum_}")