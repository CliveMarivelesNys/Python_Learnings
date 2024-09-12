import numpy as np

grocery_index = (1, 2, 3, 4)
grocery_name = ('Apple', 'Banana', 'Carrot', 'Dairy')
grocery_productcode = (101, 102, 103, 104)
grocery_quantity = (50, 100, 200, 80)
grocery_price = (0.99, 0.59, 1.29, 2.49)

grocerylist_database = np.array((0, 6, 5), dtype=object)


def grocerylist_interface():

    while True:
        grocerylist_display()
        print("")
        print("1. Change Information")
        print("2. Delete Information")
        print("0. Return to Main Menu")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            index = int(input("Enter the Index you want to edit: "))
        elif choice == 2:
            index = int(input(""))


def grocerylist_display():
    if len(grocerylist_database) == 0:
        print("The database is empty.")
    else:
        print(grocerylist_database)

def grocerylist_changeinformation(index):
    if len(grocerylist_database) == 0:
        print("The database is empty.")
    else:
        itemlookup = index - 1
        # grocery_name[itemlookup] =

grocerylist_interface()