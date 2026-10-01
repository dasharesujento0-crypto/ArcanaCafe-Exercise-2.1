MENU = {
    "Moonlight Burger": 89.00, "Stardust Chicken": 129.00,
    "Enchanted Spaghetti": 99.00, "Pixie Fries": 59.00,
    "Mystic Burger Steak": 109.00, "Galaxy Fizz": 45.00,
    "Moonbeam Iced Tea": 49.00, "Dreamy Sundae": 39.00,
    "Moonlight Burger Meal": 129.00, "Stardust Chicken Meal": 169.00,
    "Enchanted Spaghetti Meal": 139.00
}
MENU_CATEGORIES = {
    "MAIN DISHES": ["Moonlight Burger","Stardust Chicken","Mystic Burger Steak"],
    "PASTA AND RICE": ["Enchanted Spaghetti"], "SIDES": ["Pixie Fries"],
    "DRINKS": ["Galaxy Fizz","Moonbeam Iced Tea"], "DESSERTS": ["Dreamy Sundae"],
    "MEAL COMBOS": ["Moonlight Burger Meal","Stardust Chicken Meal","Enchanted Spaghetti Meal"]
}
def display_menu():
    print("\n" + "-"*68); print(" "*28+"OUR MENU"); print("-"*68)
    n = 1
    for category in MENU_CATEGORIES:
        print(f"\n{category}"); print("-"*68)
        for item in MENU_CATEGORIES[category]:
            print(f"{n:>2}. {item:<42}PHP {MENU[item]:>8.2f}"); n += 1
    print("-"*68)
def get_menu_item():
    items = [item for category in MENU_CATEGORIES for item in MENU_CATEGORIES[category]]
    while True:
        choice = input("\nEnter the number of the item you want to order: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(items):
            return items[int(choice)-1]
        print("Please enter a valid menu number.")
