check_out = False
# Create the Store Inventory
products = {
    "EnderMan": 1.67,
    "Zombie  ": 2.67,
    "Creeper ": 3.67,
    "Skeleton": 4.67,
    "Spider  ": 5.67
}
# The list of products
mob_list = list(products)
# Create the Shopping Cart
shopping_cart = {}
# Create the Main Menu
def menu():
    print("|---------------------------|")
    print("|    Minecraft mob store    |")
    print("|---------------------------|")
    print("| (1) Available mobs        |")
    print("| (2) Add mobs              |")
    print("| (3) Remove mobs           |")
    print("| (4) View Cart             |")
    print("| (5) Current total         |")
    print("| (6) Checkout              |")
    print("|---------------------------|")
# Available products
def option1():
    print()
    print("----------------------")
    print("|  products / price  |")
    print("----------------------")
    # use for loop to print out every product and their price, use i as the number in front
    i = 1
    for x, y in products.items():
        print(f"| {i}) {x} ${y}  |")
        i += 1
    print("----------------------")
    print()
def option2():
    print()
    what = int(input("What do you want: "))
    # make to user enter avaliable items
    while what < 1 or what > 5:
        print("Chose from 1 ~ 5")
        what = int(input("What do you want: "))
    how_many = int(input("How many do you want: "))
    # make the user enter a avaliable amount of items
    while how_many < 1:
        print("Please enter a number greater than zero")
        how_many = int(input("How many do you want: "))
    # add product and amount to shopping cart
    if mob_list[what - 1] in shopping_cart:
        shopping_cart[mob_list[what - 1]] += how_many
    else:
        shopping_cart[mob_list[what - 1]] = how_many

    print(f"Added {how_many} {mob_list[what - 1]}to your cart")
    print(f"There is now {shopping_cart[mob_list[what - 1]]} {mob_list[what - 1]}in the cart")
    print()
def option3():
    print()
    print("  your shopping cart  ")
    print("======================")
    # use for loop to print out every product and their price, use i as the number in front
    i = 1
    for x, y in shopping_cart.items():
        print(f" {i}) {x} * {y}")
        i += 1
    print()
    # list of every price of an item in the shooping cart
    values_in_shopping_cart = list(shopping_cart.values())
    # list of the items in the shopping cart
    list_of_items_in_shopping_cart = list(shopping_cart)
    # ask the user what they want to remove and have to be available items
    rm = int(input("What do you want to remove: "))
    while rm < 1 or rm > len(shopping_cart):
        print(f"Please choose a number between 1 ~ {len(shopping_cart)}")
        rm = int(input("What do you want to remove: "))
    # ask the user how many do they want to remove and avaliable amount
    num_to_rm = int(input("How many do you want to remove: "))
    while num_to_rm < 1 or num_to_rm > values_in_shopping_cart[rm - 1]:
        print("Can't remove that much ammount")
        num_to_rm = int(input("How many do you want to remove: "))
    # make change to the shopping cart
    shopping_cart[list_of_items_in_shopping_cart[rm - 1]] -= num_to_rm
    print()
    print(f"Remove {num_to_rm} {list_of_items_in_shopping_cart[rm - 1]}from your cart")
    print(f"You now have {(values_in_shopping_cart[rm - 1]) - num_to_rm} {list_of_items_in_shopping_cart[rm - 1]}in the cart")
    print()
def option4():
    print()
    print("~~~~~~~~~~~~~~~~~ Your shopping cart ~~~~~~~~~~~~~~~~~")
    print("    Product  /  Unit price  /  Quantity  /  Line total")
    # i be the front of lines with products, and list information of the current shopping cart
    i = 1
    total_items = 0
    subtotal = 0
    for x, y in shopping_cart.items():
        print(f"{i})  {x}      ${products[x]}           {y}           ${y * (products[x])}")
        i += 1
        total_items += y
        subtotal += y * (products[x])
    print()
    print(f"Total items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
def option5():
    # calculate for current total in the shopping cart using a for loop
    current_total = 0
    for x, y in shopping_cart.items():
        current_total += y * (products[x])
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"~~~ Current total: ${current_total} ~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
def option6():
    # import datetime into python
    import datetime
    # set t to the time right now
    t = datetime.datetime.now()
    # make time into month/day/year
    format_month_date_year = t.strftime("%m/%d/%Y")

    print("========== RECEIPT ==========")
    print("")
    # print out the date format from the begining out the program
    print("Date:", format_month_date_year)
    option4()
    # calculate if there will be discount
    current_total = 0
    for x, y in shopping_cart.items():
        current_total += y * (products[x])
    discount = 0
    if current_total < 10:
        discount = 0
    elif current_total < 20:
        discount = 5
    elif current_total < 40:
        discount = 10
    else:
        discount = 40
    if discount == 0:
        print("Discount: No discount")
    else:
        print(f"Discount: {discount}%")
    # print out the discount
    print(f"Amount Saved: ${(current_total * discount / 100):.2f}")
    # the final total
    print(f"Final total: ${current_total - (current_total * discount / 100)}")
    
while check_out != True:
    menu()
    choice = int(input("What do you want to do: "))
    if choice == 1:
        option1()
    elif choice == 2:
        option2()
    elif choice == 3:
        # Not allow if no item in the shopping cart
        if len(shopping_cart) == 0:
            print("You have nothing in your shopping cart")
        else:
            option3()
    elif choice == 4:
        option4()
    elif choice == 5:
        option5()
    elif choice == 6:
        option6()
        # end the while loop
        check_out = True
    else:
        print("Please enter a number from 1 to 6 :)")
print()
print("THANKS FOR SHOPPING :)")