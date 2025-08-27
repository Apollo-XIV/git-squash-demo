from textwrap import dedent
from adder import adder

print("DEMO PROGRAMS")

selection = input(dedent('''
    Select a number from the list to run a program:
    1. Adder
'''))

try:
    if int(selection) == 1:
        adder()
    else:
        print("I couldn't recognise your input, please provide a number from the list")
except:
    print("Invalid input, make sure you enter an integer")
