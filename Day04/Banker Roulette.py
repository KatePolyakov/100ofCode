import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]



#1st options
print(random.choice(friends))

#2nd choice
random_friend = random.randint(0, 4)
print(f'{friends[random_friend]} will pay for bill')

