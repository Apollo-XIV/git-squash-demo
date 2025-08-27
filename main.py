from textwrap import dedent
from adder import adder
import eight_ball

print("DEMO PROGRAMS")

selection = input(dedent('''
    Select a number from the list to run a program:
    1. Adder
    2. 8 Ball
'''))

try:
    if int(selection) == 1:
        adder()
    elif int(selection) == 2:
        eight_ball.ask()
    else:
        print("I couldn't recognise your input, please provide a number from the list")
except:
    print("Invalid input, make sure you enter an integer")
