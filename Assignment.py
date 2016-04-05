__JaredMarcolongo__ = 'jc321013'

""" CP1404 Assignment 1 - 2016
    Items for Hire - a console-based item hiring program
    Jared Marcolongo
    21/03/2016
    https://github.com/jc321013/Cp1404-Assignment-1 """

""" Pseudocode:

function main()
    display title of document and name
    display how many items loaded from items.csv
    open csv file of in stock items
    close csv file
    display items
    display menu
    get choice
    while choice is not 'Q'
        if choice is 'L'
            display items
        else if choice is 'H'
            call hiring_an_item()
        else if choice is 'R'
            return item
        else if choice is 'A'
            call loading_an_item()
        else
            display invalid choice message
        display menu
        get choice
    print farewell message


function loading_an_item()
    
    append new item to file

open “stats.dat” as fileOut for writing
for each datum in data
write datum to fileOut
write newline to fileOut
close fileOut

function hiring_an_item()
    display available item
    get item choice
        display item chosen
    chosen item returns an * for unavailable
        display available items
    if no items available
        display unavailable message
    display menu


    """

import csv

Menu = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to stock\n(Q)uit"
Items = '\n(0). Rusty Bucket,40L bucket - quite rusty,0,in\n(1). Golf Cart,Tesla powered 250 turbo,195,out\n(2). Thermomix,TM-31,25.5,out\n(3). AeroPress,Great coffee maker,5,in\n(4). Guitar,JTV-59,12.95,in'


def main(menu):
    print("Items for Hire- by Jared Marcolongo")
    print("3 items loaded from items.csv")

# reads from csv file and displays lines in file
items = open("items.csv", "r", encoding='utf-8')
reader = csv.reader(items.readlines())
items.close()
for line in reader:
    print(line)

    print(Items)
    print(Menu)
    # .upper allows user to input both lower and upper case letters
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


# # def loading_items():
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
