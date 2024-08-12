import time
import random

# Initialize global variables for score, health, and inventory
score = 0
health = 100
inventory = []

# Function to print text with a pause
def print_pause(text):
    print(text)
    time.sleep(1)

# Function to print text with a delayed effect for each character
def print_delayed(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to check and display the player's current score
def check_score():
    print_pause(f"Your current score: {score}")

# Function to check and display the player's current health
def check_health():
    print_pause(f"Your current health: {health}")

# Function to check and display the player's inventory
def check_inventory():
    if inventory:
        print("You have the following items:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")

# Main function for choices at the village entrance
def village_entrance():
    print("\nWhat do you want to do now?")
    print("1. Go into the Forest")
    print("2. Go into the Mountains")
    print("3. Visit the River")
    print("4. Go in the abandoned house")
    print("5. Check your inventory")
    print("6. Check your score")
    print("7. Check your health")
    choice = input("What is your choice? ")
    if choice == "1":
        forest()
    elif choice == "2":
        mountains()
    elif choice == "3":
        river()
    elif choice == "4":
        abandoned_house()
    elif choice == "5":
        check_inventory()
    elif choice == "6":
        check_score()
    elif choice == "7":
        check_health()
    else:
        print("Hmm, not sure what you mean. Try again.")
        village_entrance()

# Function for the forest scenario
def forest():
    print_delayed("You are walking in the forest, it's mysterious and dark.")
    scenario = random.choice([
        'beast', 'hidden_path', 'nothing', 'treasure', 'wise_old_man',
        'mysterious_tree'
    ])
    if scenario == 'beast':
        print_delayed("Oh no! A wild beast has appeared!")
        print_delayed("\nWhat's your action?")
        print_delayed("1. Fight the beast")
        print_delayed("2. Return to the village")
        choice = input(":")
        if choice == "1":
            fight_beast()
        elif choice == "2":
            village_entrance()
        else:
            print("Hmm, not sure what you mean. Try again.")
            forest()

    elif scenario == 'hidden_path':
        print_delayed("You discover a hidden path.")
        print_delayed("\nWhat will you do now?")
        print_delayed("1. Follow the hidden path and see where it leads")
        print_delayed("2. Return to the village")
        choice = input("Your choice: ")
        if choice == "1":
            hidden_path()
        elif choice == "2":
            village_entrance()
        else:
            print("Hmm, not sure what you mean. Try again.")
            forest()

    elif scenario == 'treasure':
        find_treasure()

    elif scenario == 'wise_old_man':
        meet_wise_old_man()

    elif scenario == 'mysterious_tree':
        mysterious_tree()

    else:
        print_delayed("The forest is quiet. Nothing seems to be happening.")
        print_delayed("Try another way to go through.")
        village_entrance()

# Function to handle fighting a beast
def fight_beast():
    global score, health
    print_delayed("\nYou fight the beast bravely and defeat it!")
    score += 30
    print(f"You gain 30 points! Current score: {score}")
    health -= 10
    print(f"You lose 10 health points. Current health: {health}")
    if health <= 0:
        game_over()
    else:
        print_delayed("You completed searching in the forest.")
        print_delayed("So you must search for the monster another way.")
        village_entrance()

# Function to handle finding a hidden path
def hidden_path():
    global score
    print_delayed("\nYou follow the hidden path and find a treasure chest!")
    print_delayed("Inside the chest, you find a powerful sword.")
    print_delayed("This will help you in your fight against the monster.")
    score += 20
    print(f"You gain 20 points! Current score: {score}")
    inventory.append("Sword")
    village_entrance()

# Function to handle finding treasure in the forest
def find_treasure():
    global score
    print_delayed("\nYou stumble upon a hidden treasure chest in the forest!")
    print_delayed("Inside the chest, you find 30 gold coins.")
    score += 30
    inventory.append("Gold coins")
    print(f"You gain 30 points! Current score: {score}")
    village_entrance()

# Function to handle meeting a wise old man in the forest
def meet_wise_old_man():
    global health
    print_delayed("\nYou meet a wise old man in the forest.")
    print_delayed("He offers you a healing potion.")
    print_delayed("\nWhat's your decision?")
    print_delayed("1. Accept the potion")
    print_delayed("2. Decline and return to the village entrance")
    choice = input("Your choice: ")
    if choice == "1":
        health += 20
        print_pause(f"You gain 20 health points! Current health: {health}")
        village_entrance()
    elif choice == "2":
        village_entrance()
    else:
        print_pause("Invalid choice. Try again.")
        meet_wise_old_man()

# Function to handle encountering a mysterious tree
def mysterious_tree():
    global score
    print_delayed("\nYou come across a mysterious tree with strange carvings.")
    print_delayed("You feel a surge of energy as you touch the tree.")
    score += 10
    print(f"You gain 10 points! Current score: {score}")
    village_entrance()

# Function for the mountains scenario
def mountains():
    global score, health
    print_delayed("\nYou climb the rocky mountains and find a cave entrance.")
    print_delayed("You hear the monster's sound coming from inside the cave!")
    scenario = random.choice([
        'trap', 'nothing', 'healing_herbs', 'bandits', 'ancient_ruines'
    ])
    if scenario == 'trap':
        print_delayed("It's a trap! You narrowly escape falling rocks.")
        health -= 20
        print(f"You lose 20 health points. Current health: {health}")
        if health <= 0:
            game_over()
        else:
            print_delayed("\nWhat will you do now?")
            print_delayed("1. Enter the cave carefully")
            print_delayed("2. Return to the village")
            choice = input("Your choice: ")
            if choice == "1":
                enter_cave()
            elif choice == "2":
                village_entrance()
            else:
                mountains()

    elif scenario == 'healing_herbs':
        find_healing_herbs()

    elif scenario == 'bandits':
        encounter_bandits()

    elif scenario == 'ancient_ruines':
        find_ancient_ruines()

    else:
        enter_cave()

# Function to handle entering the cave
def enter_cave():
    print_delayed("\nYou enter the dark cave.")
    print_delayed("You can hear the monster's roars.")
    print_delayed("You might find the monster at any time.")
    encounter = random.choice(["monster", "treasure", "nothing"])
    if encounter == "monster":
        encounter_monster()
    elif encounter == "treasure":
        collect_treasure()
    elif encounter == "nothing":
        explore_further()

# Function to handle encountering a monster in the cave
def encounter_monster():
    global score
    print_delayed("\nSuddenly, a monstrous figure emerges from the shadows!")
    print_delayed("It looks like you're in for a tough fight.")
    action = input("Do you want to 1. fight or 2. escape: ")
    if action == "1":
        print_delayed("You engage in combat with the monster...")
        print_delayed("After a long battle, you defeat the monster!")
        score += 50
        print(f"You gain 50 points! Current score: {score}")
        game_over_win()
    elif action == "2":
        print_delayed("You quickly turn around and run out of the cave.")
        print_delayed("Oops, the monster caught you and killed you!")
        game_over()

# Function to handle collecting treasure in the cave
def collect_treasure():
    global score
    print_delayed("\nYou find a hidden chest filled with glittering treasure!")
    print_delayed("It seems like you hit the jackpot.")
    score += 40
    inventory.append("Treasure")
    print(f"You gain 40 points! Current score: {score}")
    mountains()

# Function to explore further in the cave
def explore_further():
    print_delayed("\nThe cave is very quiet. You find nothing of interest.")
    action = input("Do you want to 1. explore or 2. return to the village: ")
    if action == "1":
        print_delayed("\nYou explore further into the cave.")
        enter_cave()
    elif action == "2":
        village_entrance()

# Function to handle finding healing herbs in the mountains
def find_healing_herbs():
    global health
    print_delayed("\nYou find some healing herbs growing in a crevice.")
    print_delayed("You carefully pick and use them to heal your wounds.")
    health += 20
    print(f"You gain 20 health points! Current health: {health}")
    village_entrance()

# Function to handle encountering bandits in the mountains
def encounter_bandits():
    global health
    print_delayed("\nYou encounter a group of bandits in the mountains.")
    print_delayed("They demand you hand over your valuables.")
    print_delayed("\nWhat will you do?")
    print_delayed("1. Fight the bandits")
    print_delayed("2. Run away")
    action = input(": ")
    if action == "1":
        print_delayed("\nYou decide to fight the bandits.")
        if "Sword" in inventory:
            print_delayed("\nYou use your sword and defeat the bandits!")
            score += 20
            print(f"You gain 20 points! Current score: {score}")
        else:
            print_delayed("\nYou fight bravely, but the bandits overpower you.")
            health -= 30
            print(f"You lose 30 health points. Current health: {health}")
            if health <= 0:
                game_over()
    elif action == "2":
        print_delayed("\nYou decide to flee back to the village.")
        village_entrance()

# Function to handle finding ancient ruins in the mountains
def find_ancient_ruines():
    global score
    print_delayed("\nYou find ancient ruins hidden in the mountains.")
    print_delayed("Inside, you discover some ancient artifacts.")
    score += 20
    inventory.append("Ancient Artifacts")
    print(f"You gain 20 points! Current score: {score}")
    village_entrance()

# Function for the river scenario
def river():
    global score
    print_delayed("\nYou follow the path down to the river.")
    print_delayed("The river is swift and powerful.")
    print_delayed("But you notice something shiny in the water.")
    print_delayed("\nWhat will you do?")
    print_delayed("1. Dive in to retrieve the shiny object")
    print_delayed("2. Return to the village")
    choice = input(": ")
    if choice == "1":
        dive_in_river()
    elif choice == "2":
        village_entrance()

# Function to handle diving into the river
def dive_in_river():
    global health, score
    print_delayed("\nYou dive into the river and struggle against the current.")
    find = random.choice(["gem", "nothing", "drown"])
    if find == "gem":
        print_delayed("\nYou find a sparkling gem in the water!")
        score += 30
        inventory.append("Gem")
        print(f"You gain 30 points! Current score: {score}")
        village_entrance()
    elif find == "nothing":
        print_delayed("\nYou search the water but find nothing of value.")
        village_entrance()
    elif find == "drown":
        print_delayed("\nThe current is too strong! You're swept away and drown.")
        game_over()

# Function for the abandoned house scenario
def abandoned_house():
    global score
    print_delayed("\nYou approach the abandoned house.")
    print_delayed("The door creaks as you push it open.")
    print_delayed("Inside, you find cobwebs and dust everywhere.")
    find = random.choice(["ghost", "treasure", "nothing"])
    if find == "ghost":
        print_delayed("\nA ghostly figure appears before you!")
        ghost_encounter()
    elif find == "treasure":
        print_delayed("\nYou find an old chest filled with treasure!")
        score += 40
        inventory.append("Old Treasure")
        print(f"You gain 40 points! Current score: {score}")
        village_entrance()
    elif find == "nothing":
        print_delayed("\nThe house is empty and silent.")
        village_entrance()

# Function to handle a ghost encounter
def ghost_encounter():
    global score, health
    print_delayed("\nThe ghost shrieks and lunges at you!")
    print_delayed("\nWhat will you do?")
    print_delayed("1. Fight the ghost")
    print_delayed("2. Run away")
    choice = input(": ")
    if choice == "1":
        print_delayed("\nYou fight the ghost with all your might!")
        score += 50
        print(f"You gain 50 points! Current score: {score}")
        health -= 20
        print(f"You lose 20 health points. Current health: {health}")
        if health <= 0:
            game_over()
        else:
            print_delayed("\nThe ghost disappears, leaving you shaken.")
            village_entrance()
    elif choice == "2":
        print_delayed("\nYou run out of the house, your heart pounding.")
        village_entrance()

# Function to handle the game over scenario
def game_over():
    print_delayed("\nYou've been defeated.")
    print_delayed("\nGAME OVER!")
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        reset_game()
    else:
        print_delayed("Thanks for playing!")
        exit()

# Function to handle the winning scenario
def game_over_win():
    print_delayed("\nYou've defeated the monster and saved the village!")
    print_delayed("\nCONGRATULATIONS!")
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        reset_game()
    else:
        print_delayed("Thanks for playing!")
        exit()

# Function to reset the game
def reset_game():
    global score, health, inventory
    score = 0
    health = 100
    inventory = []
    village_entrance()

# Start the game
def start_game():
    print_delayed("\nWelcome to the Adventure Game!")
    print_delayed("Your mission is to defeat the monster and save the village.")
    print_pause("\nGood luck, hero!")
    village_entrance()

# Start the game by calling the start_game function
start_game()
