from classes.order import Order

class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and (1<= len(name) <= 25):
            self._name = name
        else:
            raise Exception("Invalid for customer name")

    name = property(get_name, set_name)

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        customer_ordered = []
        for order in self.orders():
            if not order.coffee in customer_ordered:
                customer_ordered.append(order.coffee)

        return customer_ordered
        
    def create_order(self, coffee, price):
        Order(self, coffee, price)