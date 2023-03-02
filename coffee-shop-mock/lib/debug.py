#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")
    ari = Customer("Ari")
    coffee = Coffee("Mocha-Frappie")
    ipdb.set_trace()
