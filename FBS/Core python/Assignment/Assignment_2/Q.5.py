# WAP to calculate selling price of book based on cost price and discount.
cp = float(input("Enter cost price of book: "))
discount = float(input("Enter discount percentage:"))

discount_amount = (cp * discount) / 100
sp = cp - discount_amount

print("selling price of book =", sp)
