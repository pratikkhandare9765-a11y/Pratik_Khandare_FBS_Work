# convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

total_inches = (feet * 12) + inches

centimeter = total_inches * 2.54
meter = centimeter / 100

print("distance in meters =", meter)
print("distance in centimeters =", centimeter)
