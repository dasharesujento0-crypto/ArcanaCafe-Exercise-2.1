def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes","y"): return True
        if answer in ("no","n"): return False
        print("Please answer yes or no.")

def get_customer_name():
    while True:
        name = input("\nMay I know your name? : ").strip()
        if not name:
            print("Please enter a valid name."); continue
        if any(c.isdigit() for c in name):
            print("A name cannot contain numbers. Please try again."); continue
        return name

def get_order_type():
    while True:
        print("\n"+"-"*58); print(" "*20+"ORDER TYPE"); print("-"*58)
        print("1. Dine-in"); print("2. Takeout"); print("-"*58)
        choice = input("Choose your order type: ").strip()
        if choice == "1": return "Dine-in"
        if choice == "2": return "Takeout"
        print("Please choose 1 for Dine-in or 2 for Takeout.")

def get_quantity():
    while True:
        value = input("Enter quantity: ").strip()
        if not value.isdigit():
            print("Please enter a valid quantity."); continue
        quantity = int(value)
        if quantity <= 0:
            print("Quantity must be greater than zero."); continue
        if quantity > 50:
            print("Sorry, the maximum quantity per item is 50."); continue
        return quantity

def get_payment(total):
    print("\n"+"-"*58); print(f"{'Your final order total:':<35} PHP {total:>10.2f}")
    while True:
        try:
            payment = float(input("Enter payment amount: PHP ").strip())
            if payment < 0: print("Payment cannot be negative.")
            elif payment < total: print(f"Insufficient payment. You still need PHP {total-payment:.2f}.")
            else: return payment
        except ValueError:
            print("Please enter a valid amount.")
