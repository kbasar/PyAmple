'''
While loop in action. Create a menu and an exit option. this will repeat user input and display except 'quit'

'''
current_num = 1
while current_num <= 5:
    print (current_num)
    current_num += 1

prompt = "\nEnter your msg here, I will repeat "
prompt += "\n Enter 'quit' to exit/end "
msg = ''
while msg != 'quit':
    msg = raw_input(prompt)
    # Dont print 'quit' to repeat
    if msg != 'quit':
        print (msg)
