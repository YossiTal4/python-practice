def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

# Call the function with different values
result1 = calculate_discount(200, 10)
result2 = calculate_discount(500, 25)

print(f"Price after 10% discount: {result1}")
print(f"Price after 25% discount: {result2}")