
def adder():
    try:
        a = int(input("Enter the first number to add:\n"))
        b = int(input("Enter the second number to add:\n"))
        print(f"You got: {a + b}")
    except:
        print("Invalid input!")
