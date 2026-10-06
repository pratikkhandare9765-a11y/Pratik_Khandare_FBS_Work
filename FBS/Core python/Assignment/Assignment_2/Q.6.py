# WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12%of basic, hra=15% of basic.

basic = float(input("Enter basic salary: "))

da = (10 * basic) / 100
ta = (12 * basic) / 100
hra = (15 * basic) / 100

total_salary = basic + da + ta + hra

print("Basic salary =", basic)
print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total_salary)