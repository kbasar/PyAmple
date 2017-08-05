"""
functions are very important in python
they are like a equation with some inputs and results as output
Function can have positional arguments where order is matter to parameter or Keyword Arguments where parameter name along with value is passed to function.
Let's return a value from function. Lets give function arbitrary number of arguments as parameters.
"""


def make_pizza(*toppings):
    """argument as name tupple, * indicates it can take as many arguments as user can supply but all will be created under tupple named toppings"""
    print ("\nMaking a piza with following toppings: ")
    for topping in toppings:
        print ("\n- " + topping)

pizzahot = "'Apple', 'Meat', 'Mushroom, 'Cheese'"
make_pizza(pizzahot)
make_pizza('Apple', 'Chicken', 'Chream')
