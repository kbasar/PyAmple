'''
While loop in action with continue statement.
Create multiple options and dont' execute below continue statement unless condition matches..

This will repeat user input and display only ODD number. If even number enters by user, it ignores and asked again to re-enter another number
Application: Game, MENU, selection of multiple choice
'''

prompt = "\nEnter your ODD number, I will confirm if it is ODD: "

num = 0

while num <= 10:
    num = input(prompt)
    if (num % 2) == 0:
        continue  # this will re-start the loop from begining, ignore the any code next nellow it
    print "ODD number =\n"
    print (num)
