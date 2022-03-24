# menuy.py - list style menu
import  random

main_menu = {
    "Appetizer": ["Garlic Bread", "Onion Rings", "Chips"],
    "Beverage": ["Lemonade", "Water", "Coca Cola"],
    "Main Dish": ["Pizza", "Pasta", "Burgers"],
    "Dessert": ["Ice Cream", "Cake", "Confections"]
}

# Submenu
# Works similarly to main_menu
sub_menu = {
    "Pizza": ["Cheese", "Pepperoni", "Combo"],
    "Pasta": ["Lasagna", "Fettuccine", "Macaroni and Cheese"],
    "Burgers": ["Cheeseburger", "Hamburger", "Double Burger"]
}


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
def menu():
    order =[]
    title = "David's Restaurant Menu" + banner
    print(title)
    counter = 1
    for i in main_menu.keys():
        print(counter, i)
        counter = counter + 1
        random.shuffle(main_menu.get(i))
        for j in main_menu.get(i):
            print("\t", j)
        choice = input()
        order.append(i+":"+choice)
    print("Your order is: ", order)

if __name__ == "__main__":
    menu()