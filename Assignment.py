__JaredMarcolongo__ = 'jc321013'


""" CP1404 Assignment 1 - 2016
    Items for Hire - a console-based item hiring program
    Jared Marcolongo
    21/03/2016 """
# two functions : loading items and hring an item

Menu = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"
Items = "0.Rusty Bucket: 40L bucket - quite rusty	= $0\n1.AeroPress: Great coffee maker = $5\n2.Guitar:	JTV-59	$12.95"


print("Items for Hire- by Jared Marcolongo")
print("3 items loaded from items.csv")

print(Menu)
print(Items)
choice = input("Enter your choice: ").upper()
while choice != "Q":
    if choice == "L":
        print(Items)
    elif choice == "H":
        hiring_an_item()
        item = input("enter the number of an item to hire: ")
        print(item, "hired for", cost)
        print(Menu)
        choice = input("Enter your choice: ").upper()
    elif choice == "R":
        return_item = input("enter the number of an item to return: ")
        print(return_item, "returned")
        print(Menu)
        choice = input("Enter your choice: ").upper()
    elif choice == "A":
        item_name = input("Item Name: ")
        print(item_name)
        item_description = input("Description: ")
        print(item_description)
        item_price = input("Price per day: ")
        print("$", item_price)
        print(item_name, (item_description), item_price, "now available for hire")
        print(Menu)
        choice = input("Enter your choice: ").upper()
    else:
        print("Invalid menu choice.")
        print(Menu)
        choice = input("Enter your choice: ").upper()

    print("5 items saved to items.csv\n" "Have a nice day")


def loading_items():


    def hiring_an_item():
        print("All items on file(* indicates item is currently out\n)", Items)
        hire = input("Enter the number of an item to hire: ")
        print(hire)
        while choice == "H":
            if hire == "0":
                print("Rusty Bucket hired for $0.00")
            print(Menu)
            choice = input("Enter your choice: ").upper()
            # elif choice == "1":















