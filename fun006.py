"""
functions are very important in python
they are like a equation with some inputs and results as output

Function can have positional arguments where order is matter to parameter or Keyword Arguments where parameter name along with value is passed to function.

Let's return a value from function. Return Dictionary and List.

"""


def name_dict(firstname, lastname='basar'):
    """format the first & last name into dictionry and return"""
    name_dic = {'first': firstname, 'last': lastname}
    return name_dic


person = name_dict('Abu', 'Abdullah')
print person
print (name_dict('Khairul', 'Basar'))
