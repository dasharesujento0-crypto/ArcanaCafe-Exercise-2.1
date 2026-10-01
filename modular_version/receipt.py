from datetime import datetime
def generate_receipt_number(): return datetime.now().strftime("AC-%Y%m%d-%H%M%S")
def get_date_time(): return datetime.now().strftime("%B %d, %Y %I:%M %p")
