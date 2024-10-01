import random

# Game Data
locations = ["the borough", "a picnic area", "under a rock", "a flower patch"]
food_items = ["crumb", "steak", "chip"]
ant_health = 3
food_collected = 0

def display_status():
    print(f"\nYou are in {current_location}.")
    print(f"Health: {ant_health}")
    print(f"Food collected: {food_collected}")

def explore():
    global current_location
    current_location = random.choice(locations)
    print(f"\nYou explore {current_location}.")

def collect_food():
    global food_collected
    food = random.choice(food_items)
    food_collected += 1
    print(f"\nYou found a {food}! Total food collected: {food_collected}")

def encounter_enemy():
    global ant_health
    print("\nOh no! You encountered a hungly spider!")
    action = input("Do you want to (f)ight or (r)un? ")
    
    if action.lower() == 'f':
        result = random.choice(["won", "lost"])
        if result == "won":
            print("You bravely fought off the spider!")
        else:
            ant_health -= 1
            print("You got hurt! Health decreased.")
    elif action.lower() == 'r':
        print("You ran away safely!")

def game_over():
    print("\nGame Over! You have no health left.")
    exit()

# Main Game Loop
current_location = random.choice(locations)

print("Fractal Reverie: The Labyrinth of Shadows")
while True:
    display_status()
    
    action = input("\nWhat do you want to do? (e)xplore, (c)ollect food, (q)uit: ")
    
    if action.lower() == 'e':
        explore()
        if random.random() < 0.5:  # 50% chance of encountering an enemy
            encounter_enemy()
            if ant_health <= 0:
                game_over()
    elif action.lower() == 'c':
        collect_food()
    elif action.lower() == 'q':
        print("Thanks for playing!")
        break
    else:
        print("Invalid action! Please choose again.")