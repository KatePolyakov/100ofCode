# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


#greet_with_name("Jack Bauer")

#Function with multiple inputs

def multiple_inputs(name, wife_name):
    print(f"Hello {name}")
    print(f"How is {wife_name}?")

#multiple_inputs('Vova', 'Kate')

#function so that it prints the expected values.

def my_function(a, b):
    print(b)
    print(a)

#my_function(2, 1)

#Keyword Arguments

def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')

#greet_with(location="London", name='Kate')

#LOVE CALCULATOR
def calculate_love_score(name1, name2):
    word1 = 'true'
    word2 = 'love'
    word1_count = 0
    word2_count = 0
    two_names = name1 + ' ' +name2

    for letter in two_names:
        if letter in word1:
            word1_count += 1

    for letter in two_names:
        if letter in word2:
            word2_count += 1
    result = str(word1_count)+str(word2_count)

    print(result)

calculate_love_score('Angela Yu', 'Jack Bauer')