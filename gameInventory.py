import csv

# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification
# Displays the inventory.


def display_inventory(inventory):
    print("Inventory:")
    for key, value in inventory.items():
        print(inventory[key], key)
    print("Total number of items: " + str(sum(inventory.values())))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print("Inventory: ")
    x = 0
    max_len = 0
    for key in inventory:
        x = len(str(key))
        if max_len < x:
            max_len = int(x)
    count_list = list(inventory.items())
    t = 0

    if order == "ascending":
        for l in range(len(count_list)):
            for i in range(len(count_list) - 1):
                if count_list[i][1] > count_list[i + 1][1]:
                    t = count_list[i]
                    count_list[i] = count_list[i + 1]
                    count_list[i + 1] = t
    elif order == "descending":
        for l in range(len(count_list)):
            for i in range(len(count_list) - 1):
                if count_list[i][1] < count_list[i + 1][1]:
                    t = count_list[i]
                    count_list[i] = count_list[i + 1]
                    count_list[i + 1] = t

    print("Count".rjust(5), "Item name".rjust(max_len + 3))
    print('-'.rjust(max_len + 9, '-'))
    for i in range(len(count_list)):
        print(str(count_list[i][1]).rjust(5),
              str(count_list[i][0]).rjust(max_len + 3))
    print("-".rjust(max_len + 9, "-"))
    print("Total number of items: ", sum(inventory.values()))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    with open("import_inventory.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",",)
        for import_inventory in reader:
            for item in import_inventory:
                if item in inventory:
                    inventory[item] += 1
                else:
                    inventory[item] = 1


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    count_list = list(inventory.items())
    inventory_list = []
    for i in range(len(count_list)):
        for t in range(count_list[i][1]):
            inventory_list.append(str(count_list[i][0]))
    s = ",".join(inventory_list)
    with open(filename, 'w') as writecsv:
        writecsv.write(s)
    writecsv.close


'''inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory(inv)
add_to_inventory(inv, dragon_loot)
display_inventory(inv)
import_inventory(inv, "import_inventory.csv")
display_inventory(inv)
print_table(inv, "descending")
import_inventory(inv, "loot.csv")
display_inventory(inv)
export_inventory(inv, )'''