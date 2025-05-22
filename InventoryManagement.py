def main():
    global stock_items
    stock_items = []
    print("Welcome to the Inventory Management System")
    while True:
        print(
            "1. Enter stock items\n"
            "2. View current inventory\n"
            "3. Add new item\n"
            "4. Delete item\n"
            "5. Update item quantity\n"
            "6. Update item name\n"
            "7. Exit"
        )
        choice = int(input("Enter the number with your choice: "))
        if choice == 1:
            enter_stock_items()

        elif choice == 2:
            view_current_inventory()

        elif choice == 3:
            add_new_item()

        elif choice == 4:
            delete_item()

        elif choice == 5:
            update_item_quantity()

        elif choice == 6:
            update_item_name()
        elif choice == 7:
            print("Exiting the Inventory Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


def enter_stock_items():
    while True:
        item = input("Enter the name of the item or done to finish: ")
        if item.lower() == "done":
            break
        else:
            quantity = int(input("Enter the quantity of the item: "))
            stock_items.append({"item": item, "quantity": quantity})
            print(
                f"{item} has been added to the inventory with a quantity of {quantity} units."
            )
            print(stock_items)
            print("")
    return stock_items


def view_current_inventory():
    if not stock_items:
        print("No items in the inventory.")
        print("")
        return
    else:
        print("Current Inventory:")
        for index, item in enumerate(stock_items):
            print(f"{index + 1}. {item['item']} - {item['quantity']} units")
        print("")


def add_new_item():
    view_current_inventory()
    new_item = input("Enter the name of the new item: ")
    new_quantity = int(input("Enter the quantity of the new item: "))
    stock_items.append({"item": new_item, "quantity": new_quantity})
    print(
        f"{new_item} has been added to the inventory with a quantity of {new_quantity} units."
    )
    print(stock_items)
    print("")


def delete_item():
    view_current_inventory()
    item_to_delete = int(input("Enter the number of the item you want to delete: ")) - 1
    if 0 <= item_to_delete < len(stock_items):
        stock_items.pop(item_to_delete)
        print("Item deleted successfully.")
        print(stock_items)
    else:
        print("Invalid item number.")
    print("")


def update_item_quantity():
    view_current_inventory()
    item_to_update = (
        int(input("Enter the number of the item whose quantity you want to update: "))
        - 1
    )
    if 0 <= item_to_update < len(stock_items):
        new_quantity = int(input("Enter the new quantity: "))
        stock_items[item_to_update]["quantity"] = new_quantity
        print(
            f"{stock_items[item_to_update]['item']} quantity updated to {new_quantity} units."
        )
        print(stock_items)
    else:
        print("Invalid item number.")
    print("")


def update_item_name():
    view_current_inventory()
    to_update = (
        int(input("Enter the number of the item whose name you want to update: ")) - 1
    )
    if 0 <= to_update < len(stock_items):
        new_name = input("Enter the new name: ")
        stock_items[to_update]["item"] = new_name
        print(f" Name updated to {new_name}.")
        print(stock_items)
    else:
        print("Invalid item number.")
    print("")


main()
