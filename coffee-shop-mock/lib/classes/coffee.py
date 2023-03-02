from classes.order import Order

class Coffee:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and not hasattr(self, "_name"):
            self._name = name

    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        customer_ordered_coffee = []
        for order in self.orders():
            if not order.customer in customer_ordered_coffee:
                customer_ordered_coffee.append(order.customer)

        return customer_ordered_coffee
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        coffee_price = [order.price for order in self.orders()]
        return sum(coffee_price)/ len(coffee_price)