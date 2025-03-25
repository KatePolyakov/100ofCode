def format_name(f_name, l_name):

    if f_name == '' or l_name == '':
        return 'You didn\'t write your first name or last name'
    else:
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"{formated_f_name} {formated_l_name}"


#print(format_name(input('Please write your first name: '), input('Please write your last name: ')))


#Leap Year

def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

print(is_leap_year(2100))