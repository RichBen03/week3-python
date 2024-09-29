def discounting(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter your discount percent: "))

# Call the function to calculate the final price
final_price = discounting(original_price, discount_percent)

# Print the final result
if final_price != original_price:
    print(f"The final price after discounting is {final_price:.2f}")
else:
    print(f"No discount applied. Original price is {original_price:.2f}")
