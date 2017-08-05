"""
functions are very important in python
they are like a equation with some inputs and results as output

Function can have positional arguments where order is matter to parameter or Keyword Arguments where parameter name along with value is passed to function.

Lets give function arbitrary number of arguments as parameters along with positional argument

Creating module with multiple function in it. Which function can be called by importing the module in another file

"""


def make_pizza(size, *toppings):
    """argument as name tupple, * indicates it can take as many arguments as user can supply but all will be created under tupple named toppings"""
    print ("\nMaking a piza of size " + str(size) + " with following toppings: ")
    for topping in toppings:
        print ("\n- " + topping)

# If many parameters are there in function, format them this way
def make_burger(
        size,
        *ingredients):
    """argument as name tupple, * indicates it can take as many arguments as user can supply but all will be created under tupple named toppings"""
    print ("\nMaking a Burger of size " + str(size) + " with following ingredients: ")
    for ingredient in ingredients:
        print ("- ")
        print ingredient
