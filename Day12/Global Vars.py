# Modifying Global Scope

enemies = 1

#type 1 with global scopes

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


#type 2 without global scopes
def increase_enemies_2(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1


enemies = increase_enemies_2(enemies)
print(f"enemies outside function avoid global scope : {enemies}")
