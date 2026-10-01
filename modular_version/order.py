def add_item(orders, item, quantity):
    orders[item] = orders.get(item, 0) + quantity

def calculate_order_total(orders, menu):
    return sum(menu[item] * quantity for item, quantity in orders.items())

def calculate_discount(subtotal, is_student):
    return subtotal * 0.10 if is_student else 0

def calculate_final_total(subtotal, discount):
    return subtotal - discount

def calculate_change(payment, total):
    return payment - total
