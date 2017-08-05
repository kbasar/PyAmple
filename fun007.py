"""
functions are very important in python
they are like a equation with some inputs and results as output

Function can have positional arguments where order is matter to parameter or Keyword Arguments where parameter name along with value is passed to function.

Let's return a value from function. Return Dictionary and List.

"""


def name_list(names):
    """argument as name list and print greetings to all"""

    for name in names:
        msg = "Hello , " +name.title() + "!"
        print (msg)

username = ['Raju', 'Tukul', 'Takul', 'Geeta']
name_list(username)
