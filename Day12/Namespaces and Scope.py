#Scopes

enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Local Scope
def drink_potion():
    posion_strength = 2
    print(posion_strength)

drink_potion()
#print(posion_strength) <---- doesn't work

#global scope
health_strength = 15

def player_health():
    print(health_strength)

player_health()
print(health_strength)
