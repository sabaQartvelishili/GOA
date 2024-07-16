#Asks the use to enter the saving
savings = float(input("Shemoitanettanxa:"))
savings1 = float(input("Shemoitanettanxa:"))

#Convert the user input into a float value and update the variable
balance= savings * 1.05

#Savings grow after 1 year at 5% annual intrest rate
balance1= savings1 * 1.05

#Convert the balance into a string
message = "Amount in 1 year: ", balance

#
print(str(balance), balance1)