from datetime import datetime

class MenuItem:
    def __init__(self, name, price, category):
        self.name = name; self.price = price; self.category = category

class Menu:
    def __init__(self):
        data = [
            ("Moonlight Burger",89,"MAIN DISHES"),("Stardust Chicken",129,"MAIN DISHES"),
            ("Mystic Burger Steak",109,"MAIN DISHES"),("Enchanted Spaghetti",99,"PASTA AND RICE"),
            ("Pixie Fries",59,"SIDES"),("Galaxy Fizz",45,"DRINKS"),("Moonbeam Iced Tea",49,"DRINKS"),
            ("Dreamy Sundae",39,"DESSERTS"),("Moonlight Burger Meal",129,"MEAL COMBOS"),
            ("Stardust Chicken Meal",169,"MEAL COMBOS"),("Enchanted Spaghetti Meal",139,"MEAL COMBOS")
        ]
        self.items = [MenuItem(*x) for x in data]
    def display(self):
        print("\n"+"-"*68); print(" "*28+"OUR MENU"); print("-"*68)
        category = None
        for n,item in enumerate(self.items,1):
            if item.category != category:
                category = item.category; print(f"\n{category}\n"+"-"*68)
            print(f"{n:>2}. {item.name:<42}PHP {item.price:>8.2f}")
        print("-"*68)

class Customer:
    def __init__(self, name, order_type):
        self.name = name; self.order_type = order_type; self.is_student = False

class Order:
    def __init__(self):
        self.items = {}
    def add_item(self, item, quantity):
        self.items[item.name] = self.items.get(item.name, {"item":item,"quantity":0})
        self.items[item.name]["quantity"] += quantity
    def subtotal(self):
        return sum(x["item"].price*x["quantity"] for x in self.items.values())
    def discount(self, customer):
        return self.subtotal()*0.10 if customer.is_student else 0
    def final_total(self, customer):
        return self.subtotal() - self.discount(customer)
    def display(self):
        print("\n"+"-"*58); print(" "*20+"CURRENT ORDER"); print("-"*58)
        for x in self.items.values():
            item=x["item"]; qty=x["quantity"]; total=item.price*qty
            print(f"{item.name:<28}{qty:>4}{'PHP':>7}{total:>10.2f}")
        print("-"*58); print(f"{'Current Total':<28}{'':>4}{'PHP':>7}{self.subtotal():>10.2f}"); print("-"*58)

class Receipt:
    def __init__(self, customer, order, payment):
        self.customer=customer; self.order=order; self.payment=payment
        self.number=datetime.now().strftime("AC-%Y%m%d-%H%M%S")
    def display(self):
        subtotal=self.order.subtotal(); discount=self.order.discount(self.customer); total=self.order.final_total(self.customer)
        change=self.payment-total; date=datetime.now().strftime("%B %d, %Y %I:%M %p")
        print("\n"+"="*58); print(" "*19+"ARCANA CAFÉ"); print(" "*15+"ENCHANTED RESTAURANT"); print("="*58)
        print(f"Receipt No. : {self.number}"); print(f"Customer    : {self.customer.name}"); print(f"Order Type  : {self.customer.order_type}"); print(f"Date        : {date}")
        print("-"*58); print(f"{'Item':<28}{'Qty':>4}{'Price':>11}{'Total':>11}"); print("-"*58)
        for x in self.order.items.values():
            item=x["item"]; qty=x["quantity"]; print(f"{item.name:<28}{qty:>4}{item.price:>11.2f}{item.price*qty:>11.2f}")
        print("-"*58); print(f"{'Subtotal:':<35} PHP {subtotal:>10.2f}")
        label="Student discount (10%):" if self.customer.is_student else "Student discount:"
        print(f"{label:<35} PHP {discount:>10.2f}"); print(f"{'Final total:':<35} PHP {total:>10.2f}")
        print(f"{'Payment:':<35} PHP {self.payment:>10.2f}"); print(f"{'Change:':<35} PHP {change:>10.2f}")
        print("="*58); print(" "*14+"Thank you for visiting Arcana Café!"); print(" "*14+"May your day be filled with wonder."); print("="*58)

class ArcanaCafe:
    def __init__(self): self.menu=Menu()
    def yes_no(self,prompt):
        while True:
            x=input(prompt).strip().lower()
            if x in ("yes","y"): return True
            if x in ("no","n"): return False
            print("Please answer yes or no.")
    def name(self):
        while True:
            x=input("\nMay I know your name? : ").strip()
            if x and not any(c.isdigit() for c in x): return x
            print("Please enter a valid name.")
    def order_type(self):
        while True:
            print("\n1. Dine-in\n2. Takeout")
            x=input("Choose your order type: ").strip()
            if x=="1": return "Dine-in"
            if x=="2": return "Takeout"
            print("Please choose 1 or 2.")
    def quantity(self):
        while True:
            x=input("Enter quantity: ").strip()
            if x.isdigit() and 0<int(x)<=50: return int(x)
            print("Enter a quantity from 1 to 50.")
    def payment(self,total):
        while True:
            try:
                x=float(input(f"Enter payment amount (PHP {total:.2f}): "))
                if x>=total: return x
                print("Insufficient payment.")
            except ValueError: print("Please enter a valid amount.")
    def run(self):
        while True:
            print("\n"+"="*68+"\n"+" "*24+"ARCANA CAFÉ\n"+"="*68)
            name=self.name()
            if not self.yes_no("\nWould you like to place an order? (yes/no): "):
                print("Thank you for visiting Arcana Café!"); break
            customer=Customer(name,self.order_type()); order=Order()
            while True:
                self.menu.display()
                while True:
                    x=input("\nEnter the number of the item you want to order: ").strip()
                    if x.isdigit() and 1<=int(x)<=len(self.menu.items): break
                    print("Please enter a valid menu number.")
                item=self.menu.items[int(x)-1]; qty=self.quantity(); order.add_item(item,qty)
                print(f"Added {qty} x {item.name} to your order."); order.display()
                if not self.yes_no("\nWould you like to add another item? (yes/no): "): break
            print("\n"+"-"*58+"\nSTUDENT DISCOUNT\n"+"-"*58)
            customer.is_student=self.yes_no("Are you a student? (yes/no): ")
            order.display()
            subtotal=order.subtotal(); discount=order.discount(customer); total=order.final_total(customer)
            print(f"\nSubtotal: PHP {subtotal:.2f}\nStudent discount: PHP {discount:.2f}\nFinal total: PHP {total:.2f}")
            payment=self.payment(total); Receipt(customer,order,payment).display()
            if not self.yes_no("\nWould you like to serve another customer? (yes/no): "):
                print("Thank you for using Arcana Café!"); break

if __name__=="__main__": ArcanaCafe().run()
