"""
Debugging Odd or Even
- Read the code in exercise.py
- Spot the problems 🐞.
- Modify the code to fix the program.
Fix the code so that it works and passes the tests when you submit.
"""

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

print("Odd or even: ", odd_or_even(73))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print('Is Leap? ', is_leap(2000))

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(25)