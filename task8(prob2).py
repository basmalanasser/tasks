def calculate_bread_price(num_loaves):
 regular_price_per_loaf=3.49
 discount_percentage=0.06

 total_regular_price=num_loaves*regular_price_per_loaf
 discount=total_regular_price*discount_percentage
 total_price=total_regular_price-discount

 return total_regular_price,discount,total_price

num_of_loaves=int(input("enter the number of loaves:"))
regular_price,discount,total_price=calculate_bread_price(num_of_loaves)

print("Regular price:",regular_price)
print("Discount",discount)
print("Total price:",total_price)