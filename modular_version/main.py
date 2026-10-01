import os
from menu import MENU, display_menu, get_menu_item
from input_validation import ask_yes_no, get_customer_name, get_order_type, get_quantity, get_payment
from order import add_item, calculate_order_total, calculate_discount, calculate_final_total, calculate_change
from display import display_header, display_welcome, display_order_summary, display_price_summary, display_receipt
from receipt import generate_receipt_number, get_date_time

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        display_header()
        name = get_customer_name(); display_welcome(name)
        if not ask_yes_no("\nWould you like to place an order? (yes/no): "):
            print("\nThank you for visiting Arcana Café!\nHave a wonderful day!"); break
        order_type = get_order_type()
        orders = {}
        while True:
            display_menu(); item = get_menu_item(); quantity = get_quantity()
            add_item(orders, item, quantity)
            print(f"\nAdded {quantity} x {item} to your order."); display_order_summary(orders, MENU)
            if not ask_yes_no("\nWould you like to add another item? (yes/no): "): break
            print("\nReturning to the menu...")
        subtotal = calculate_order_total(orders, MENU)
        print("\n"+"-"*58+"\nSTUDENT DISCOUNT\n"+"-"*58+"\nStudents can receive a 10% discount.")
        student = ask_yes_no("Are you a student? (yes/no): ")
        discount = calculate_discount(subtotal, student); final = calculate_final_total(subtotal, discount)
        display_order_summary(orders, MENU); display_price_summary(subtotal, discount, final, student)
        payment = get_payment(final); change = calculate_change(payment, final)
        display_receipt(name, order_type, orders, MENU, subtotal, discount, final, payment, change, generate_receipt_number(), get_date_time(), student)
        if not ask_yes_no("\nWould you like to serve another customer? (yes/no): "):
            print("\nThank you for using Arcana Café!\nThe program has ended."); break
        input("\nPreparing the system for the next customer...\nPress Enter to continue...")

if __name__ == "__main__": main()
