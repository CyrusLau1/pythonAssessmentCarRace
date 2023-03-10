# @author: cyrus
# I am building a car racing game called "Turbo Titans" using Python. You are allowed to make
# this a console program β text-based, or make it visual using libraries like Pygame.
# In this game users choose a car (numbered 1 to 12).
# Then they choose a βrace distanceβ which should be between 5 and 15.
# A random number from 1-12 is generated and if the carβs number comes up, the car moves forward one space.
# The user can choose to race again after a race.


import random
import time

# Welcomes the user and introduces the game
print("Welcome to π₯Turbo Titansπ₯! \nIn this game, you can choose a car (numbered 1 to 12). \nThen, you can "
      "choose a the distance of the race, which is be between 5 and 15. \nAfter the race starts, a "
      "random number from 1-12 is generated each turn, \nand if the carβs number comes up, the car "
      "moves forward one space. \nThe winning car is the one which completes the race distance the first. π")

# Ask if the user wants to start
while True:
    begin = input("Would you like to start? Your answer: ").lower().strip()
    if begin == "yes":
        print("β Starting the game...")
        break
    elif begin == "no":
        print("β")
        exit()
    else:
        print("Please enter either yes or no.")

# Shows a list of cars available
garage = ["(1)  π", "(2)  π", "(3)  π", "(4)  π", "(5)  π", "(6)  π", "(7)  π", "οΈ(8)  π",
          "(9)  π", "(10) π", "(11) π", "(12) π»", " "]
print("\nCars in garage: ")
for item in garage:
    print(item)

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

# Ready to start the race
print("\nStarting the race...")
time.sleep(1)
print("3!")
time.sleep(1)
print("2!")
time.sleep(1)
print("1!")
time.sleep(1)
print("πGO!π")


cars = {1: "(1)  π",
        2: "(2)  π",
        3: "(3)  π",
        4: "(4)  π",
        5: "(5)  π",
        6: "(6)  π",
        7: "(7)  π",
        8: "οΈ(8)  π",
        9: "(9)  π",
        10: "(10) π",
        11: "(11) π",
        12: "(12) π»"
        }

# Sets up the starting positions for the cars
positions = {car: 0 for car in cars}


# Function to generate a random number and move the cars
def rng():
    turn = 0
    while True:
        rand_num = random.randint(1, 12)  # Generates a random number between 1 and 12
        if 5 <= distance < 8:  # Speeds up each turn depending on the distance
            time.sleep(0.6)
        elif 8 <= distance < 12:
            time.sleep(0.4)
        elif 12 <= distance <= 15:
            time.sleep(0.25)
        turn += 1
        print("π" * (4 + distance))
        print(f"~Turn {turn}~")
        print("Generating random number...\n"
              f"Number generated: {rand_num}. Car number {rand_num} will move forward one space.")

        # Check if any of the cars move forward
        for car in cars:
            if rand_num == car:  # Moves a car forward 1 'space' (2 spaces in reality)
                positions[car] += 2
        time.sleep(0.25)
        # Print the current race standings
        print("π" * (4 + distance))
        for car in cars:
            print(f"{cars[car]}:{' ' * positions[car]}βπ¨")


# Check if any car has won the race
        for car in cars:
            if positions[car] == distance * 2:
                print("π" * (4 + distance))
                time.sleep(1.5)
                print(f"\nπ Car {car} has moved {distance} spaces! Car {car} wins! π")
                if car == chosen_car:  # Shows that the user won
                    print("π Victory! Your car has won! π")
                else:  # Shows that the user lost
                    print(f"π³ Defeat... Your car only moved {positions[chosen_car] / 2 :.0f} spaces.")
                while True:  # Ask if user wants to race again
                    race_again = input(
                        f"Would you like to start another race? Your chosen car (car {chosen_car}) and the race "
                        f"track ({distance} spaces) will remain the same. Your answer: ").strip().lower()
                    if race_again == "yes":  # Starts another race
                        for car in cars:
                            positions[car] = 0
                        print("Starting another race...")
                        time.sleep(1.5)
                        rng()
                    elif race_again == "no":  # Thanks the user and ends the game
                        print("Thanks for playing π₯Turbo Titansπ₯!")
                        exit()
                    else:
                        print("Please enter either yes or no.")


# Calls the function
rng()
