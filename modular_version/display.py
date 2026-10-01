def display_header():
    print("="*68); print(" "*24+"ARCANA CAFÉ"); print(" "*20+"ENCHANTED RESTAURANT")
    print("="*68); print(" "*16+"Where every meal holds a little wonder."); print("="*68)

def display_welcome(name): print(f"\nWelcome to Arcana Café, {name}!")

def display_order_summary(orders, menu):
    subtotal = 0
    print("\n"+"-"*58); print(" "*20+"CURRENT ORDER"); print("-"*58)
    for item, quantity in orders.items():
        total = menu[item] * quantity; subtotal += total
        print(f"{item:<28}{quantity:>4}{'PHP':>7}{total:>10.2f}")
    print("-"*58); print(f"{'Current Total':<28}{'':>4}{'PHP':>7}{subtotal:>10.2f}"); print("-"*58)

def display_price_summary(subtotal, discount, final_total, is_student):
    print("\n"+"-"*58); print(f"{'Subtotal:':<35} PHP {subtotal:>10.2f}")
    label = "Student discount (10%):" if is_student else "Student discount:"
    print(f"{label:<35} PHP {discount:>10.2f}")
    print(f"{'Final total:':<35} PHP {final_total:>10.2f}"); print("-"*58)

def display_receipt(name, order_type, orders, menu, subtotal, discount, final_total, payment, change, receipt_no, date_time, student):
    print("\n"+"="*58); print(" "*19+"ARCANA CAFÉ"); print(" "*15+"ENCHANTED RESTAURANT"); print("="*58)
    print(f"Receipt No. : {receipt_no}"); print(f"Customer    : {name}"); print(f"Order Type  : {order_type}"); print(f"Date        : {date_time}")
    print("-"*58); print(f"{'Item':<28}{'Qty':>4}{'Price':>11}{'Total':>11}"); print("-"*58)
    for item, qty in orders.items():
        print(f"{item:<28}{qty:>4}{menu[item]:>11.2f}{menu[item]*qty:>11.2f}")
    print("-"*58); print(f"{'Subtotal:':<35} PHP {subtotal:>10.2f}")
    label = "Student discount (10%):" if student else "Student discount:"
    print(f"{label:<35} PHP {discount:>10.2f}"); print(f"{'Final total:':<35} PHP {final_total:>10.2f}")
    print(f"{'Payment:':<35} PHP {payment:>10.2f}"); print(f"{'Change:':<35} PHP {change:>10.2f}")
    print("="*58); print(" "*14+"Thank you for visiting Arcana Café!"); print(" "*14+"May your day be filled with wonder."); print("="*58)
