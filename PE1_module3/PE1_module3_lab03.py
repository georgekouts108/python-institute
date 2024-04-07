income = float(input("Enter the annual income: "))

#
# Write your code here.
#
tax = 0

if income <= 85528:
    tax = (0.18 * income) - 556.02
else:
    surplus_tax = (income - 85528) * 0.32
    tax = 14839.02 + surplus_tax

if tax <= 0:
    tax = 0.0
    
tax = round(tax, 0)
print("The tax is:", tax, "thalers")
