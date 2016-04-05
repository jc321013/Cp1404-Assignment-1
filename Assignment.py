__JaredMarcolongo__ = 'jc321013'


""" CP1404 Assignment 1 - 2016
    Items for Hire - a console-based item hiring program
    Jared Marcolongo
    21/03/2016 """

import csv




Menu = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"
Items = "\n0.Rusty Bucket: 40L bucket - quite rusty = $0\n1.AeroPress: Great coffee maker = $5\n2.Guitar:	JTV-59	$12.95"


def main(menu):
    print("Items for Hire- by Jared Marcolongo")
    print("3 items loaded from items.csv")

in_file = open("items.csv", "r", encoding='utf-8')
reader = csv.reader(in_file.readlines())
in_file.close()
for line in reader:
    print(line)

    print(Items)
    print(Menu)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "L":
            print(line)
        elif choice == "H":
            hiring_an_item()
            choice = input("Item number: ").upper()
        elif choice == "R":
            return_item = input("Number of an item to return: ")
            print(return_item, "returned")
        elif choice == "A":
            item_name = input("Item Name: ")
            print(item_name)
            item_description = input("Description: ")
            print(item_description)
            item_price = input("Price per day: ")
            print("$", item_price)
            print(item_name, item_description, item_price, "now available for hire")
        else:
            print("Invalid menu choice.")
        print(Menu)
        choice = input("Enter your choice: ").upper()

        print("5 items saved to items.csv\n" "Have a nice day")


#     # def loading_items():
#     #     print("")
#     #
#     # def hiring_an_item():
#     #     print("All items on file(* indicates item is currently out\n)", Items)
#     #     hiring_choice = input("Enter the number of an item to hire: ")
#     #     print(hiring_choice, "hired for")
#     #     while hiring_choice == "H":
#     #         if hiring_choice == "0":
#     #             print("Rusty Bucket hired for $0.00")
#     #             print(Menu)
#     #         elif hiring_choice == "1":
#     #             print("AeroPress: Great coffee maker hired for $5")
#     #
#     #
#     #
#     #         print(Menu)
#
# main(Menu)
#
#
#
#
#
#
#
#
#
#
#
