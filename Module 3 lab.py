# Melanie Perfitt
# (CIS 129 Spring 2024)
# Module 3 lab
# 2/14/2024

#Variables
cost_of_muffin = 4
cost_of_coffee = 5
cost_of_tea = 3
cost_of_mug = 6

#Constant - a variable that you dont change
TAX = .06

#print statement for formatting
print("***************************************")

#Input statements
coffees_bought = int(input("Number of coffess bought? "))
print(coffees_bought)
muffins_bought = int(input("Number of muffins bought?"))
print(muffins_bought)
tea_bought = int(input("Number of tea bought? "))
print(tea_bought)
mugs_bought = int(input("Number of mugs bought? "))

#print statement for formatting
print("***************************************")
print()
print()
print("***************************************")


#Processing
#Calculates the total cost of individual goods
muffin_total_bought = cost_of_muffin * muffins_bought
coffees_total_bought = cost_of_coffee * coffees_bought
tea_total_bought = cost_of_tea * tea_bought
mug_total_bought = cost_of_mug * mugs_bought

#Calculcates the total before sales tax
total_before_tax = muffin_total_bought + coffees_total_bought + tea_total_bought + mug_total_bought


#Calculates base tax
base_tax = total_before_tax * TAX

#Calculates final total
final_total = total_before_tax + base_tax

#Output section
print("My coffee and Muffin shop receipt")
print(coffees_bought , "Coffee at $" , cost_of_coffee , "each: $" , coffees_total_bought)
print(muffins_bought , "Muffins at $" , cost_of_muffin , "each: $" , muffins_bought)
print(tea_bought , "Tea at $" , cost_of_tea , "each: $" , tea_bought)
print(mugs_bought , "Mugs at $" , cost_of_mug , "each: $" , mugs_bought)

print("6% tax: $" , base_tax)
print("---------")
print("Total: #" ,  final_total)

print("Thank you for choosing your local Coffee Shop!")
print("***************************************")


