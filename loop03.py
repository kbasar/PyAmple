'''
While loop in action with break statement.
Create a menu and an exit option.
While loop runs as long as some variable is not equals to 'quit' and ends when 'quit' is entered.
This will repeat user input and display except 'quit'
Application: Game, MENU, selection of multiple choice
'''

prompt = "\nEnter your city here, I will repeat  except 'quit'"
prompt += "\n Enter 'quit' to exit/end "

while True:
    city = raw_input(prompt)
    # Dont print 'quit' to repeat
    if city == 'quit':
        break  # this will end while loop here, without it this while loop if infinite
    else:
        print (city)
