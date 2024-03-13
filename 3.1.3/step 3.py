sandwhich_type = ""
sandwhich_price = ""
subtotal = 0.0

# Explaining menu options
print("What type of sandwhich would you like?")
print("Chicken $5.25, beef $6.25, tofu $5.75")
sandwhich_type = input("Sandwhich Choice: ")

# Calculating sandwhich type
order = []

if sandwhich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    order.append("chicken")
    subtotal += 5.25
elif sandwhich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    order.append("tofu")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    order.append("beef")
    subtotal += 6.25

beverage_choice = ""
beverage_price = ""

beverage_choice = input("Do you wish to add a beverage: ")
if beverage_choice == "yes":
    beverage_choice = input("What size: Small $1.00, Medium $1.75, Large $2.25")
    if beverage_choice == "Small":
        print("You chose small, which will be $1.00")
        order.append("Small")
        subtotal += 1.00
    elif beverage_choice == "Medium":
        print("You chose Medium, which will be $1.75")
        order.append("Medium")
        subtotal += 1.75
    else:
        print("You chose Large, which will be $2.25")
        order.append("Large")
        subtotal += 2.25

# Fries go here
fries_choice = ""
print("Would you like to add fries with your order?")
fries_choice = input("")
if fries_choice == "yes":
    print("What size of fries would you like?")
    print("Small $1.00, Medium $1.50, Large $2.00)")
    fries_choice = input("Which size of fries would you like?")
    if fries_choice == "Small":
        print("Would you like to mega size your fries?")
        fries_choice = input("")

    elif fries_choice == "Medium":
        print("You chose Medium, which will be $1.50")
        order.append("Medium")
        subtotal += 1.50
    else:
        print("You chose Large, which will be $2.00")
        order.append("Large")
        subtotal += 2.00



print("Your total will be")
print(subtotal)