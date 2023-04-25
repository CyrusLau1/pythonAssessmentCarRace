# @author: cyrus
# I am building a car racing game called "Turbo Titans" using Python.
# In this game users choose a car (numbered 1 to 12).
# Then they choose a ‘race distance’ which should be between 5 and 15.
# Then they choose the game speed, which should be between 1 and 5
# A random number from 1-12 is generated and if the car’s number comes up,
# the car moves forward one space
# The user can choose to race again after finishing a race.

import random
import time
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Welcomes the user and introduces the game
print(f"Welcome to {Fore.RED}{Style.BRIGHT}🔥Turbo Titans🔥{Fore.RESET}{Style.NORMAL}! "
      f"\nIn this game, you can choose a {Style.BRIGHT}car (numbered 1 to 12){Style.NORMAL}. "
      f"\nThen, you can choose the {Style.BRIGHT}distance {Style.NORMAL}of the race, "
      f"which must be {Style.BRIGHT}between 5 and 15{Style.NORMAL}. "
      f"\nYou can also choose the {Style.BRIGHT}speed{Style.NORMAL} at which the game progresses."
      f"\nAfter the race starts, a random number from 1-12 is generated each turn, "
      f"\nand if the car’s number comes up, the car moves forward one space. "
      f"\nThe winning car is the one which completes the race distance the first. 🏆"
      f"\nAfter each race, you will earn {Fore.YELLOW}coins 🪙 {Fore.RESET}(300 for winning, 100 for losing), "
      f"which you can use to buy {Fore.BLUE}upgrades ⬆️ {Fore.RESET}in the shop. "
      f"\nThese upgrades will help you win more, earn more coins , and ultimately become the richest Turbo Titan!🔥"
      f"\n{Fore.RED}Reminder: Your car, the distance and the speed cannot be changed once chosen unless you exit the game. "
      f"\nAll coins and upgrades do {Style.BRIGHT}NOT{Style.NORMAL} save after you exit the game.")

# Ask if the user wants to start
while True:
    start = input("Would you like to start? Your answer: ").lower().strip()
    if start == "yes":
        print(Fore.GREEN + "✅ Starting the game...")
        break
    elif start == "no":
        print(Fore.RED + "❌ Exiting...")
        exit()
    else:
        print("Please enter either yes or no.")

# Shows a list of cars available in the garage
garage = ["(1)  🚜", "(2)  🚌", "(3)  🚚", "(4)  🚐", "(5)  🚑", "(6)  🚒", "(7)  🚓", "️(8)  🚕",
          "(9)  🚗", "(10) 🚙", "(11) 🚛", "(12) 🛻", " "]
print("\nCars in garage: ")
for c in garage:
    print(c)

# Ask the user to choose a car number and validate it
while True:
    try:
        chosen_car = int(input("Please choose your race car's number (from 1 to 12). Your choice: "))
        if 1 <= chosen_car <= 12:
            print(f"You have chosen car number {chosen_car}. You win if car number {chosen_car} wins.")
            break
        else:
            print("This car does not exist. Please choose a number between 1 and 12.")
    except ValueError:
        print("Please enter a valid integer.")

# Ask the user to choose a distance for the race and validate it
while True:
    try:
        distance = int(input("Now, please choose the distance for the race (from 5 to 15). Your answer: "))
        if 5 <= distance <= 15:
            print(f"The distance is {distance}. This means if a car moves {distance} spaces, it wins.")
            break
        else:
            print("This is not an appropriate distance for the race. "
                  "Please enter a number between 5 and 15.")
    except ValueError:
        print("Please enter a valid integer.")

# Ask the user to choose the speed for the game
while True:
    try:
        speed = float(input("Please enter the speed that the game progresses at (from 1 to 5). The higher "
                            "the speed, the shorter time it will take for each turn to progress.\nThis does "
                            "not affect the results of the race in any way. Enter 1 to proceed with the "
                            "default speed.\nYour answer: "))
        if 1 < speed <= 5:
            print(f"The game will progress {speed} times faster.")
            break
        elif speed == 1:
            print("The game will proceed at the default speed.")
            break
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a valid number.")


# A function that announces the start of the race
def ready():
    print("\nStarting the race...")
    time.sleep(1)
    print(Fore.RED + "3!")
    time.sleep(1)
    print(Fore.YELLOW + "2!")
    time.sleep(1)
    print(Fore.GREEN + "1!")
    time.sleep(1)
    print(Style.BRIGHT + "🎌GO!🎌\n")


# Sets up the starting positions for the cars
cars = {1: "(1)  🚜",
        2: "(2)  🚌",
        3: "(3)  🚚",
        4: "(4)  🚐",
        5: "(5)  🚑",
        6: "(6)  🚒",
        7: "(7)  🚓",
        8: "(8)  🚕",
        9: "(9)  🚗",
        10: "(10) 🚙",
        11: "(11) 🚛",
        12: "(12) 🛻"
        }

positions = {car: 0 for car in cars}

# Sets up the values of some variables which will be needed later in the game
coins = 0
coin_multi = 1
space_multi = 0
buddy = 0
injured = 0
headstart = 0

# Sets up a list to show the upgrades available in the shop
upgrades = [
    f"[1] {Fore.GREEN}Money, Money, Money!{Fore.RESET}: "
    f"The amount of coins you earn after a race is doubled.{Fore.YELLOW}(200🪙)",
    f"[2] {Fore.GREEN}Injured Racer{Fore.RESET}: "
    f"Choose a random racer to be injured and forfeit the race, causing their car to "
    f"be unable to move.{Fore.YELLOW}(200🪙)",
    f"[3] {Fore.GREEN}Head Start{Fore.RESET}: "
    f"Your car is positioned one space forward before the start of the race.{Fore.YELLOW}(300🪙)",
    f"[4] {Fore.GREEN}Buddies{Fore.RESET}: "
    f"Choose another racer to become your buddy. You also win if their car wins.{Fore.YELLOW}(500🪙)",
    f"[5] {Fore.GREEN}Turbo Titans Champions{Fore.RESET}: "
    f"You and your buddy's cars (if Buddies is purchased) move forward two spaces instead of one when they get "
    f"chosen.{Fore.YELLOW}(800🪙)"
]

# Sets up the user's inventory, empty at first, bought upgrades will show up here
inventory = []


# Sets up the shop where user can buy powerful upgrades, shows up after each race
def shop():
    global coins
    global coin_multi
    global space_multi
    global buddy
    global injured
    global headstart

    while True:
        try:  # Asks whether the user would like to open the shop ,or inventory
            open_shop = input("Would you like to open the shop to buy upgrades? Enter 'yes' to open shop, 'no' to "
                              "skip, \nor enter 'inventory' to see all purchased upgrades. Your answer: ")

            if open_shop == "yes":
                print(Fore.BLUE + "⬆️ Shop: ")  # Shows the upgrades available in the shop
                if len(upgrades) == 0:  # If user has already bought all upgrades, show this message
                    print("You have already bought all the upgrades. Good luck becoming the richest Turbo Titan in the "
                          "universe!")
                    break
                for u in upgrades:
                    print(u)
                while True:
                    try:
                        purchase = input(  # Ask the user what they want to purchase
                            f"You have {Fore.YELLOW}{coins}🪙{Fore.RESET}. \n"
                            f"[Type 'close' to close the shop]\n"
                            f"What would you like to buy? Type the number of the bonus you want to purchase: ") \
                            .strip().lower()

                        if purchase == "1" and coin_multi == 2:  # If they have already bought this upgrade, show this (same for other upgrades)
                            print(Fore.RED + "You have already purchased this upgrade.")
                        elif purchase == "1" and coins >= 200:  # Checks whether the user has enough money to buy the upgrade (same for other upgrades)
                            print(Fore.GREEN + "You have purchased Money, Money, Money!")
                            coin_multi += 1
                            upgrades.remove(f"[1] {Fore.GREEN}Money, Money, Money!{Fore.RESET}: "  # Removes this upgrade from shop
                                            f"The amount of coins you earn after a race is doubled.{Fore.YELLOW}(200🪙)")
                            inventory.append(f"[1] {Fore.GREEN}Money, Money, Money!{Fore.RESET}: "  # Adds this upgrade to inventory
                                             f"The amount of coins you earn after a race is doubled.{Fore.YELLOW}(200🪙)")
                            coins -= 200  # Deduct coins from balance
                        elif purchase == "1" and coins < 200:
                            print(Fore.RED + "Insufficient amount of coins.")
                        elif purchase == "2" and injured != 0 and injured != chosen_car:
                            print(Fore.RED + "You have already purchased this upgrade.")
                        elif purchase == "2" and coins >= 200:
                            injured += int(input("Please choose a racer to be injured. Enter their car number: "))
                            if injured == chosen_car:
                                print("Please do not injure yourself.")
                                injured -= chosen_car
                            else:
                                coins -= 200
                                upgrades.remove(f"[2] {Fore.GREEN}Injured Racer{Fore.RESET}: "
                                                f"Choose a random racer to be injured and forfeit the race, causing their car to "
                                                f"be unable to move.{Fore.YELLOW}(200🪙)")
                                inventory.append(f"[2] {Fore.GREEN}Injured Racer{Fore.RESET}: "
                                                 f"Choose a random racer to be injured and forfeit the race, causing their car to "
                                                 f"be unable to move.{Fore.YELLOW}(200🪙)")
                                print(Fore.GREEN + "You have purchased Injured Racer.")
                                print(f"Racer or car number {injured} will be injured and will forfeit the race.")
                        elif purchase == "2" and coins < 200:
                            print(Fore.RED + "Insufficient amount of coins.")
                        elif purchase == "3" and headstart != 0:
                            print(Fore.RED + "You have already purchased this upgrade.")
                        elif purchase == "3" and coins >= 300:
                            print(Fore.GREEN + "You have purchased Head Start.")
                            headstart += 1
                            upgrades.remove(f"[3] {Fore.GREEN}Head Start{Fore.RESET}: "
                                            f"Your car is positioned one space forward before the start of the race.{Fore.YELLOW}(300🪙)")
                            inventory.append(f"[3] {Fore.GREEN}Head Start{Fore.RESET}: "
                                             f"Your car is positioned one space forward before the start of the race.{Fore.YELLOW}(300🪙)")
                            coins -= 300
                        elif purchase == "3" and coins < 300:
                            print(Fore.RED + "Insufficient amount of coins.")
                        elif purchase == "4" and buddy != 0:
                            print(Fore.RED + "You have already purchased this upgrade.")
                        elif purchase == "4" and coins >= 500:
                            buddy += int(input("Please choose a racer to become your buddy. Enter their car number: "))
                            if buddy == chosen_car:
                                print("Please do not choose yourself as your buddy.")
                                buddy -= chosen_car
                            elif buddy == injured:
                                print("Please do not choose an injured racer to be your buddy.")
                                buddy -= injured
                            else:
                                print(Fore.GREEN + "You have purchased Buddies.")
                                print(f"Racer of car number {buddy} will now be your buddy.")
                                upgrades.remove(f"[4] {Fore.GREEN}Buddies{Fore.RESET}: "
                                                f"Choose another racer to become your buddy. You also win if their car wins.{Fore.YELLOW}(500🪙)")
                                inventory.append(f"[4] {Fore.GREEN}Buddies{Fore.RESET}: "
                                                 f"Choose another racer to become your buddy. You also win if their car wins.{Fore.YELLOW}(500🪙)")
                                coins -= 500
                        elif purchase == "4" and coins < 500:
                            print(Fore.RED + "Insufficient amount of coins.")
                        elif purchase == "5" and space_multi == 2:
                            print(Fore.RED + "You have already purchased this bonus.")
                        elif purchase == "5" and coins >= 800:
                            print(Fore.GREEN + "You have purchased Turbo Titan Champions.")
                            space_multi += 2
                            upgrades.remove(f"[5] {Fore.GREEN}Turbo Titans Champions{Fore.RESET}: "
                                            f"You and your buddy's cars (if Buddies is purchased) move forward two spaces instead of one when they get "
                                            f"chosen.{Fore.YELLOW}(800🪙)")
                            inventory.append(f"[5] {Fore.GREEN}Turbo Titans Champions{Fore.RESET}: "
                                             f"You and your buddy's cars (if Buddies is purchased) move forward two spaces instead of one when they get "
                                             f"chosen.{Fore.YELLOW}(800🪙)")
                            coins -= 800
                        elif purchase == "5" and coins < 800:
                            print(Fore.RED + "Insufficient amount of coins.")
                        elif purchase == "close":  # Closes the shop
                            print("Closing shop...")
                            break
                        else:  # If the user doesn't enter an expected input
                            print("Please enter a number between 1 and 5 or 'close'.")
                    except ValueError:
                        print("Please enter a valid input.")
            elif open_shop == "no":  # Continues the game if user says no
                print("Continuing game...")
                break
            elif open_shop == "inventory":  # Opens the user's inventory
                print(Fore.BLUE + "⬆️ Owned Upgrades: ")
                for i in inventory:
                    print(i)
            else:
                print("Enter either yes or no!")

        except ValueError:
            print("Please enter a valid input.")


# Function to generate a random number and move the cars
def rng():
    global coins
    global coin_multi
    global space_multi
    global buddy
    global injured
    global headstart

    ready()
    turn = 0
    while True:
        rand_num = random.randint(1, 12)  # Generates a random number between 1 and 12
        if 5 <= distance <= 8:  # Speeds up each turn depending on the distance and speed selected
            time.sleep(0.75 / speed)
        elif 8 < distance < 12:
            time.sleep(0.5 / speed)
        elif 12 <= distance <= 15:
            time.sleep(0.25 / speed)

        turn += 1
        print("🏁" * (4 + distance))
        print(f"~Turn {turn}~")  # Shows the number of turns
        print("Generating random number...\n"
              f"Number generated: {rand_num}. Car number {rand_num} will move forward one space.")

        # Check if any of the cars move forward
        for car in cars:
            if rand_num == car:  # Moves a car forward 1 'space' (2 spaces in reality --> easier to notice movement)
                positions[car] += 2
                positions[injured] = 0
                if car == chosen_car:
                    positions[car] += space_multi
                elif car == buddy:
                    positions[car] += space_multi
        time.sleep(0.3 / speed)
        # Print the current race standings
        print("🏁" * (4 + distance))  # Creates the racetrack
        for car in cars:
            print(f"{cars[car]}:{' ' * positions[car]}‍💨")

        # Check if any car has won the race
        for car in cars:
            if positions[car] == distance * 2:
                print("🏁" * (4 + distance))
                time.sleep(1.5)
                print(f"\n🏁 It took {turn} turns for car {car} to move {distance} spaces! Car {car} wins! 🎉")
                if car == chosen_car:  # Shows that the user won and give the corresponding amount of coins
                    print(Fore.GREEN + "🏆 Victory! Your car has won! 🎉")
                    print(f"You have earned {Fore.YELLOW}{300 * coin_multi}🪙!")
                    coins += 300 * coin_multi
                elif car == buddy:
                    print(Fore.GREEN + "🏆 Victory! You and your buddy have won the race! 🎉")
                    print(f"You have earned {Fore.YELLOW}{300 * coin_multi}🪙!")
                    coins += 300 * coin_multi
                else:  # Shows that the user lost and the number of spaces their car moved
                    print(Fore.RED + f"🏳 Defeat... Your car only moved {positions[chosen_car] / 2 :.0f} spaces.")
                    print(f"You have earned {Fore.YELLOW}{100 * coin_multi}🪙!")
                    coins += 100 * coin_multi
                print(f"You now have {Fore.YELLOW}{coins}🪙.")  # Total amount of coins user hsa
                shop()  # The shop shows up here
                while True:  # Ask if user wants to race again
                    race_again = input(
                        f"Would you like to start another race? Your chosen car (car {chosen_car}), race "
                        f"track ({distance} spaces) and game speed ({speed}x) will remain the same. "
                        f"\nYour answer: ").strip().lower()
                    if race_again == "yes":  # Starts another race
                        for car_a in cars:  # Resets car positions
                            positions[car_a] = 0
                            if headstart == 1:
                                positions[chosen_car] = 2
                            else:
                                positions[chosen_car] = 0
                        print("Starting another race...")
                        time.sleep(1.5)
                        rng()
                    elif race_again == "no":  # Thanks the user and ends the game
                        confirm_exit = input("Exit the game? Your answer: ")
                        if confirm_exit == "yes":  # Asks user to confirm exiting the game
                            print(f"Thanks for playing {Fore.RED}{Style.BRIGHT}🔥Turbo Titans🔥{Fore.RESET}{Style.NORMAL}!")
                            exit()
                        elif confirm_exit ==  "no":
                            continue
                        else:
                            print("Enter either yes or no.")
                    else:
                        print("Please enter either yes or no.")


# Calls the function
rng()
