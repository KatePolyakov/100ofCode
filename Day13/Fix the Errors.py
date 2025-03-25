
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You did not enter a number, please re-enter")
    age = int(input("How old are you? "))


if age > 18:
    print(f"You can drive at age {age}.")
