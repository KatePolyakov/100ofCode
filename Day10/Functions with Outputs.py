#function with outputs
def my_function(num1, num2):
    result = num1*num2
    return result

output =my_function(3, 2)

print(output)
print(my_function(4, 2))

def format_name(first_name, last_name):
    return first_name.capitalize() + ' ' + last_name.capitalize()

full_name = (format_name('kaTe', 'polyakov'))

print(type(full_name))

print(format_name('kaTe', 'polyakov'))

def function_1(text):
    return text+' ' + text

def function_2(text):
    return text.capitalize()

output_2 = function_1('hello')
output_3 = function_2((function_1('hello')))
print(output_2)
print(output_3)