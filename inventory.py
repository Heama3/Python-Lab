inventory = {
    "apple": 10,
    "banana": 20,
    "orange": 15
}
item = input("Enter the item name to sell: ")
quantity = int(input("Enter quantity to sell: "))


if item in inventory:
    if inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"Sold {quantity} {item}.")
        print(f"Remaining {item}: {inventory[item]}")
    else:
        print(f"Not enough stock. Only {inventory[item]} {item} available.")
else:
    print("Item not found in inventory.")
