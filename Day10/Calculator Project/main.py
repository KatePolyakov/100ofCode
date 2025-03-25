import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

#print(operation['*'](4, 8))
#print(multiply(4, 8))

"""multiply ===== operation[type of operation]"""


def calculator():
    print(art.logo)
    continue_working = True
    number_1 = float(input('Type the first number? '))

    while continue_working:

        operator = input('Type a mathematical operator (a choice of "+", "-", "*" or "/") ')
        number_2 = float(input('Type the second number? '))
        result = (operation[operator](number_1, number_2))
        print(f"The result is: {result}")

        same_result = input("Do you want to continue working with the previous result? y or n ")
        if same_result == 'y':
            number_1 = result

        elif same_result == 'n':
            continue_working = False
            calculator()

calculator()
