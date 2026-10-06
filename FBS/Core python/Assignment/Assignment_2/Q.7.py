# find the sum of three-digit number

num = int(input("Enter a three-digits number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum = a + b + c

print("sum of three digits =", sum)