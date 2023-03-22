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
      f"which must be {Style.BRIGHT}between 5 and 15{Style.NORMAL}. \nAfter the race starts, "
      f"a random number from 1-12 is generated each turn, \nand if the car’s number comes up, "
      f"the car moves forward one space. "
      f"\nThe winning car is the one which completes the race distance the first. 🏆")

# Ask if the user wants to start
while True:
    begin = input("Would you like to start? Your answer: ").lower().strip()
    if begin == "yes":
        print(Fore.GREEN + "✅ Starting the game...")
        break
    elif begin == "no":
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
        speed = float(input("Please enter the speed that the game progresses (from 1 to 5). The higher "
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
        8: "️(8)  🚕",
        9: "(9)  🚗",
        10: "(10) 🚙",
        11: "(11) 🚛",
        12: "(12) 🛻"
        }

positions = {car: 0 for car in cars}


# Function to generate a random number and move the cars
def rng():
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
        print(f"~Turn {turn}~")
        print("Generating random number...\n"
              f"Number generated: {rand_num}. Car number {rand_num} will move forward one space.")

        # Check if any of the cars move forward
        for car in cars:
            if rand_num == car:  # Moves a car forward 1 'space' (2 spaces in reality)
                positions[car] += 2
        time.sleep(0.3 / speed)
        # Print the current race standings
        print("🏁" * (4 + distance))
        for car in cars:
            print(f"{cars[car]}:{' ' * positions[car]}‍💨")

        # Check if any car has won the race
        for car in cars:
            if positions[car] == distance * 2:
                print("🏁" * (4 + distance))
                time.sleep(1.5)
                print(f"\n🏁 It took {turn} turns for car {car} to move {distance} spaces! Car {car} wins! 🎉")
                if car == chosen_car:  # Shows that the user won
                    print(Fore.GREEN + "🏆 Victory! Your car has won! 🎉")
                else:  # Shows that the user lost
                    print(Fore.RED + f"🏳 Defeat... Your car only moved {positions[chosen_car] / 2 :.0f} spaces.")
                while True:  # Ask if user wants to race again
                    race_again = input(
                        f"Would you like to start another race? Your chosen car (car {chosen_car}), race "
                        f"track ({distance} spaces) and game speed ({speed}x) will remain the same. "
                        f"\nYour answer: ").strip().lower()
                    if race_again == "yes":  # Starts another race
                        for car1 in cars:  # Resets car positions
                            positions[car1] = 0
                        print("Starting another race...")
                        time.sleep(1.5)
                        rng()
                    elif race_again == "no":  # Thanks the user and ends the game
                        print(f"Thanks for playing {Fore.RED}{Style.BRIGHT}🔥Turbo Titans🔥{Fore.RESET}{Style.NORMAL}!")
                        exit()
                    else:
                        print("Please enter either yes or no.")


# Calls the function
rng()
