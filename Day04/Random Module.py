import random
import my_module

#Random Whole Numbers Within a Range
random_number = random.randint(1, 10)
print(random_number)

print(my_module.my_favourite_number)

#Random Floats

random_float = random.random()*10
random_float_more1 = random.uniform(1, 10)
print(random_float)
print(random_float_more1)

#PAUSE 1 - Heads or Tails

random_coin_number = random.randint(1,2)

if random_coin_number == 1:
    print('Heads')
else:
    print('Tails')