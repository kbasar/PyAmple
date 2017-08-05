"""
functions are very important in python
they are like a equation with some inputs and results as output

Function can have positional arguments where order is matter to parameter or Keyword Arguments where parameter name along with value is passed to function.
Here is Keyword Arguments example

"""


def greeting(my_name, my_dog_name):
    """See how order is not important"""

    print ("Hello, " + my_name.title() + "!")
    print (" \n You have your Dog named : " + my_dog_name)

greeting(my_name='Raju', my_dog_name='fee')

# if you don't pass the arguments as per parameter order, you will not messed up like insulting Raju. function will go smooth.

greeting(my_dog_name='Fee', my_name='Raju')
