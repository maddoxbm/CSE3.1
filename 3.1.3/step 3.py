sandwhich_type = ""
sandwhich_price = ""
subtotal = 0.0

# Explaining menu options
print("What type of sandwhich would you like?")
print("Chicken $5.25, beef $6.25, tofu $5.75")
sandwhich_type = input("Sandwhich Choice: ")

# Calculating sandwhich type
if sandwhich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif sandwhich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25

beverage_choice = ""
beverage_price = ""
print("Would you like to add a beverage?")
beverage_choice = input("Do you wish to add a beverage: ")
if beverage_choice == "yes":
    print




