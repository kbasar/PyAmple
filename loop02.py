'''
While loop in action.
Create a menu and an exit option.
While loop runs as long as a flag is TRUE and ends when 'quit' is entered.
This will repeat user input and display except 'quit'
Application: Game, MENU, selection of multiple choice
'''

prompt = "\nEnter your msg here, I will repeat "
prompt += "\n Enter 'quit' to exit/end "
flag = True
while flag:
    msg = raw_input(prompt)
    # Dont print 'quit' to repeat
    if msg == 'quit':
        flag = False  # while loop stops after this
    else:
        print (msg)
