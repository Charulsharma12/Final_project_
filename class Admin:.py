class Admin:
    def __init__(self):
        self.food_items = {}
    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1
        self.food_items[food_id] = [name, quantity, price, discount, stock]

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        if food_id in self.food_items:
            self.food_items[food_id] = [name, quantity, price, discount, stock] 
    def view_all_food_items(self):
        return self.food_items
    
    def remove_food_item(self, food_id):
        if food_id in self.food_items:
            del self.food_items[food_id]

class User:
    def __init__(self):
        self.users= {}
        self.orders = {}
    def register(self, full_name, phone_number, email, address, password):
        user_id = len(self_user) + 1 
        self.user[user_id] = {
            'FullName': full_name,
            'PhoneNumber': phone_number,
            'Email': email,
            'Address': address,
            'Password': password
        }
        return user_id
    def login(self, email, password):
        for user_id, user_info in self.user.items()
            if user_info['Email'] == email and user_info['Password'] == password:
                return user_id
        return None 
    def place_new_order(self, user_id, selected_items):
        self.orders[user_id] = selected_items
    def order_history(self, user_id):
        return self.orders.get(user_id, "No orders yet")
    
    def update_profile(self, user_id, full_name = None, phone_number = None, email = None, address = None, password = None):
        if user_id in self.users:
            user = self.users[user_id]
            if full_name:
                user['FullName'] = full_name
            if phone_number:
                user['PhoneNumber'] = phone_number
            if email:
                user['Email'] = email
            if address:
                user['Address'] = address
            if password:
                user['Password'] = password
