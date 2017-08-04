"""
functions are very important in python
they are like a equation with some inputs and results as output

Function can have positional arguments where order is matter to parameter or Keyword Arguments where parameter name along with value is passed to function.

Let's return a value from function.

"""


def fullname_format(firstname, lastname='basar'):
    """format the first & last name into full name and return"""

    full_name = firstname + ' ' + lastname
    return full_name

print (fullname_format(firstname='Khairul'))

# if you don't pass the arguments as per parameter order, you will not messed up like insulting Raju. function will go smooth.

print (fullname_format('Khairul', 'Abdullah'))

"""
Optional arguments to function
"""


def name_format(firstname, middlename, lastname='basar'):
    """format the first & last name into full name, check if middle name is also there and return"""

    if middlename:
        full_name = firstname + ' ' + middlename + ' ' + lastname
    else:
        full_name = firstname + ' ' + lastname
    return full_name


print (name_format('Khairul', 'Abu', 'Basar2'))  # Positional arguments
print (name_format('Khairul', 'Basar2') + ":::")# Positional arguments, Basar2 is middle name.
