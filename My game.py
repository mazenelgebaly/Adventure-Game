import time
import random

score = 0
health = 100
inventory = []


def print_pause(text):
    print(text)
    time.sleep(1)
    # this function for sleep after print


def print_delayed(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    # this function for delaying texts it makes it more cool


def check_score():
    print_pause(f"Your current score: {score}")
    # function for checking the score of the player score


def check_health():
    print_pause(f"Your current health: {health}")
    # function for checking the score of the player health


def check_inventory():
    if inventory:
        print("You have the following items:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")
    # function for checking the score of the player inventory


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
    # this is the function for all the main choices of the player in village


def forest():
    print_delayed("You are walking in the forest,it's mysterious and dark")
    scenario = random.choice(
        ['beast', 'hidden_path', 'nothing', 'treasure', 'wise_old_man',
         'mysterious_tree'])
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
            choice = input("Your choice:")

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
        choice = input("Your choice: ")
    elif scenario == 'treasure':
        find_treasure()
    elif scenario == 'wise_old_man':
        meet_wise_old_man()
    elif scenario == 'mysterious_tree':
        mysterious_tree()
    else:
        print_delayed("The forest is quiet. Nothing seems to be happening.")
        print_delayed("Try another way to go through")
        village_entrance()
        # this is the first main scenario of the game


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
        print_delayed("You completed searching in the forest,")
        print_delayed("So you must search about the monster in another way")
        village_entrance()


def hidden_path():
    global score
    print_delayed("\nYou follow the hidden path and find a treasure chest!")
    print_delayed("Inside the chest, you find a powerful sword.")
    print_delayed("This will help you in your fight against the monster.")
    score += 20
    print(f"You gain 20 points! Current score: {score}")
    inventory.append("Sword")
    village_entrance()


def find_treasure():
    global score
    print_delayed("\nYou stumble upon a hidden treasure chest in the forest!")
    print_delayed("Inside the chest, you find 30 gold coins.")
    score += 30
    inventory.append("Gold coins")
    print(f"You gain 30 points! Current score: {score}")
    village_entrance()


def meet_wise_old_man():
    global health
    print_delayed("\nYou meet a wise old man in the forest.")
    print_delayed("He offers you a healing potion.")
    time.sleep(2)
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
        choice = input("choose again:")


def mysterious_tree():
    global score
    print_delayed("\nYou come across a mysterious tree with strange carvings."
    )
    print_delayed("You feel a surge of energy as you touch the tree.")
    score += 10
    print(f"You gain 10 points! Current score: {score}")
    village_entrance()


def mountains():
    global score, health
    print_delayed("\nYou climb the rocky mountains and find a cave entrance.")
    time.sleep(2)
    print_delayed("You hear the monster sound coming from inside the cave!")
    scenario = random.choice(
        ['trap', 'nothing', 'healing_herbs', 'bandits', 'ancient_ruines'])

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
                print("Invalid choice. Try again.")
                time.sleep(1)
                choice = input("Your Choice:")
    elif scenario == 'healing_herbs':
        find_healing_herbs()
    elif scenario == 'bandits':
        encounter_bandits()
    elif scenario == 'ancient_ruines':
        find_ancient_ruines()
    else:
        enter_cave()

    # this is the second main scenario for the game it contains many paths


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


def encounter_monster():
    global score
    print_delayed("\nSuddenly, a monstrous figure emerges from the shadows!")
    print_delayed("It looks like you're in for a tough fight.")
    action = input("Do you want to 1.fight or 2.escape: ")

    if action == 1:
        print_delayed("You engage in combat with the monster...")
        print_delayed("After a long battle, you defeat the monster!")
        score += 50
        print(f"You gain 50 points! Current score: {score}")
        game_over_win()
    elif action == 2:
        print_delayed("You quickly turn around and run out of the cave.")
        print_delayed("opps , the monster had caught you and killed you")
        game_over()
        # the final stage for the game and the player win


def collect_treasure():
    global score
    print_delayed("\nYou find a hidden chest filled with glittering treasure!"
    )
    print_delayed("It seems like you hit the jackpot.")
    score += 40
    inventory.append("Treasure")
    print(f"You gain 40 points! Current score: {score}")
    mountains()


def explore_further():
    print_delayed("\nThe cave is very quiet. You find nothing of interest.")
    action = input("Do you want to 1.explore or 2.return to the village: ")

    if action == 1:
        print_delayed(
            "You venture deeper into the cave, searching for more secrets.")
        enter_cave()
    elif action == 2:
        print_delayed("You head back to the entrance of the cave.")
        village_entrance()


def find_healing_herbs():
    global score, health
    print_delayed("\nYou find some healing herbs in the mountains.")
    health += 20
    print(f"You gain 20 health points! Current health: {health}")
    print_delayed("\nWhat will you do now?")
    print_delayed("1. Enter the cave carefully")
    print_delayed("2. Return to the village entrance")
    choice = input("Your choice: ")

    if choice == "1":
        enter_cave()
    elif choice == "2":
        village_entrance()
    else:
        print("Invalid choice. Try again.")
        choice = input("Your choice:")


def encounter_bandits():
    global score, health, inventory
    print_delayed("\nYou are ambushed by bandits in the mountains")
    item_to_check = 'sword'
    if item_to_check in inventory:
        print("you attacked them by your sword and win the battle!")
        score += 20
        print_delayed(f"you gains 20 points.current score: {score}")
    else:
        health -= 30
        print(f"You lose 30 health points. Current health: {health}")
        score -= 10
        print(f"You lose 10 points! Current score: {score}")
    if health <= 0:
        game_over()
    else:
        print_delayed("\nWhat will you do now?")
        print_delayed("1. Continue exploring the mountains")
        print_delayed("2. Go back to the village entrance")
        choice = input("Your choice: ")

        if choice == "1":
            mountains()
        elif choice == "2":
            village_entrance()
        else:
            print("Invalid choice. Try again.")
            choice = input("Your Choice:")


def find_ancient_ruines():
    global score
    print_delayed("\nYou find ancient ruines hidden in a cave.")
    time.sleep(2)
    print_delayed("The ruines reveal the monster's weakness!")
    time.sleep(2)
    score += 20
    print(f"You gain 20 points! Current score: {score}")
    village_entrance()


def river():
    global health
    print_delayed("\nYou arrive at a flowing river. The water is so clear.")
    scenario = random.choice(['fishing', 'cross_river', 'nothing',
                              'dangerous_creature'])

    if scenario == 'fishing':
        go_fishing()
    elif scenario == 'cross_river':
        cross_river()
    elif scenario == 'dangerous_creature':
        encounter_creature()
    else:
        print_delayed("You enjoy the peaceful surroundings but find nothing.")
        print_delayed("So you decides to return to the village again")
        village_entrance()


def go_fishing():
    global score
    print_delayed("\nYou cast your line and catch a big fish.")
    time.sleep(2)
    print_delayed("The fish is valuable and will help you later.")
    time.sleep(2)
    score += 15
    print(f"You gain 15 points! Current score: {score}")
    print_delayed("You finish visiting the river and returned to the village")
    village_entrance()


def cross_river():
    print_delayed("\nYou try to cross the river but find it difficult.")
    print_delayed("You might need a boat or some help.")
    print_delayed("it seems loke the wrong way to search on the monster")
    print_delayed("you must try another way...")
    village_entrance()


def encounter_creature():
    global score, health, inventory
    print_delayed("\nA dangerous creature emerges from the water!")
    print_delayed("You have to fight it to proceed.")
    item_to_check = 'sword'
    if item_to_check in inventory:
        print_delayed("Wohooo, you won the battle!")
        score += 20
        print(f"You gain 20 points. Current score: {score}")
    else:
        health -= 20
        print(f"You lose 20 health points. Current health: {health}")
    if health <= 0:
        game_over()
    else:
        print_delayed("You continue your journey searching on the monster.")
        village_entrance()


def abandoned_house():

    print_delayed("\nYou approach an old abandoned house.")
    scenario = random.choice(
        ['ghost', 'nothing', 'hidden_treasure', 'trap_door'])
    if scenario == 'ghost':
        encounter_ghost()
    elif scenario == 'hidden_treasure':
        hidden_treasure()
    elif scenario == 'trap_door':
        trap_door()
    else:
        print_delayed("The house is empty and silent. There's nothing here.")
        print_delayed("you return to the village again")
        village_entrance()


def encounter_ghost():
    global score, health
    print_delayed("\nA ghost appears and seems to be guarding something.")
    choice = input("1.Attack the ghost , 2.Run away from the house")
    if choice == 1:
        print_delayed("you killed the ghost succecfully!")
        score += 20
        print(f"You gain 20 points! Current score:{score}")
        health -= 30
        print(f"you lose 30 health points due to the battle,
        Current health:{health}")
    elif choice == 2:
        print_delayed("the ghost has caught you while you were running!!")
        score -= 30
        print(f"You lose 30 points! Current score:{score}")

    if health <= 0:
        game_over()
    else:
        print_delayed("You continue your journey searching on the monster.")

    village_entrance()


def hidden_treasure():
    global score
    print_delayed("\nYou find a hidden treasure chest in the abandoned house!"
    )
    print_delayed("Inside, you find a gun.")
    score += 25
    print(f"You gain 25 points! Current score: {score}")
    inventory.append("gun")
    print_delayed("you get out the abandoned house tryna find the monster...")
    village_entrance()


def trap_door():
    global score, health
    print_delayed("\nYou find a trap door hidden in the floor.")
    print_delayed("Opening it could be dangerous.")
    choice = input("1.open it anyway , 2.get out the house:")
    if choice == 1:
        print_delayed("OPPS You got poisoned")
        health -= 30
        print(f"You lose 30 health points. Current health: {health}")
    if health <= 0:
        game_over()
    elif choice == 2:
        print_delayed("you exit the house and return to the village")
    else:
        print("Invalid Input, try again")
        print("what is your choice 1 or be:")

    village_entrance()


def game_over():
    print_delayed("\nGame Over!")
    print_delayed("Your health is zero , so you are dead...")
    print(f"Your final score: {score}")
    play_again


def game_over_win():
    print_delayed("Game over!")
    print_delayed("VICTORY , You have beated the Monster !")
    play_again


def play_again():
    while True:
        user_input = input("Do you want to play again? (y/n): ")
        while user_input not in ["y", "n"]:
            print("Invalid input. Please enter 'y' or 'n'.")
            user_input = input("Do you want to play again? (y/n): ")
        if user_input == 'y':
            score = 0
            my_game()
        else:
            print("Thank you for your time!")
            break


def my_game():
    global score, health, inventory
    score = 0
    health = 100
    inventory = []

    while True:
        user_name = input("What's your name: ")
        if user_name.isalpha():
            print_delayed(f"Welcome, {user_name}!")
            print_delayed("Let's go through our adventure")
            break
        else:
            print("Please enter a name containing only alphabetic characters."
    )
    print_delayed("Your village has been raided by monster and he stole alot")
    print_delayed("of your treasures")
    print_delayed("Your mission is to find this monster and try to kill him")
    village_entrance()


my_game()
