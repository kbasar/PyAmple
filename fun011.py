"""
 This is the way perticular functions from a module is imported and created alias of the function name.
 """
from fun009 import make_pizza as mp, make_burger as mb

pizza = mp(15, 'Apple', 'Chicken')
burger = mb(16, 'Cheese', 'Beef')
burgerBig = mb(26, 'DoubleCheese', 'DoubleBeef')
