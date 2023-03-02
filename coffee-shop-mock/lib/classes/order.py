
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if isinstance(price, int) and (1 <= price <= 10):
            self._price = price
        else:
            raise Exception('Invalid for price')
        
    price = property(get_price, set_price)

    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        from classes.customer import Customer
        if type(customer) == Customer:
            self._customer = customer
        else:
            raise Exception("customer is not in Customer class")
        
    customer = property(get_customer, set_customer)

    def get_coffee(self):
        return self._coffee
    
    def set_coffee(self, coffee):
        from classes.coffee import Coffee
        if type(coffee) == Coffee:
            self._coffee = coffee
        # else:
        #     raise Exception("coffee is not in Coffee class")
        
    coffee = property(get_coffee, set_coffee)



