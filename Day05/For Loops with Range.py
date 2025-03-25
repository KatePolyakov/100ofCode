
#Range
for number in range(1, 11, 2):
    print(number)


#PAUSE 1 - The Gauss Challenge
total_sum = 0
for new_number in range(1, 101):
    total_sum  += new_number
print(total_sum)

#FizzBuzz
total_game = 0

for number_game in range(1, 101):
    if number_game % 3 == 0 and number_game % 5 == 0:
        print('FizzBuzz')
    elif number_game %3 == 0:
        print('Fizz')
    elif number_game %5 == 0:
        print('Buzz')
    else:
        print(number_game)

