def calculate_discount(price, discount_rate):
    """
    Calculate the discounted price given the original price and discount rate.
    
    :param price: Original price of the item
    :param discount_rate: Discount rate as a decimal (e.g., 0.2 for 20%)
    :return: Discounted price
    """
    return price * (1 - discount_rate)
# Example usage
price = 100.0  # Original price
discount_rate = 0.15 # Discount rate (15%)
discounted_price = calculate_discount(price, discount_rate)
print(f"The discounted price is: {discounted_price:.2f}")
discount = 0.3

if discount>0.2:
    print("Discount")
else:
    print("No Discount ")
if discount<0.2:
    print("No Discount")
else:
    print("Discount")