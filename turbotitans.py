# @author: cyrus
# I am building a car racing game called "Turbo Titans" using Python. You are allowed to make
# this a console program – text-based, or make it visual using libraries like Pygame.
# In this game users choose a car (numbered 1 to 12).
# Then they choose a ‘race distance’ which should be between 5 and 15.
# A random number from 1-12 is generated and if the car’s number comes up, the car moves forward one space.
import random

print("Welcome to Turbo Titans! \nIn this game, you can choose a car (numbered 1 to 12). \nThen, you can "
      "choose a the distance of the race, which is be between 5 and 15. \nAfter the race starts, a "
      "random number from 1-12 is generated each turn, \nand if the car’s number comes up, the car "
      "moves forward one space. \nThe winning car is the one which completes the race distance the first.")

# Ask if the user wants to start
while True:
    begin = input("Would you like to start? Your answer: ").lower().strip()
    if begin == "yes":
        print("✅ Starting the game...")
        break
    elif begin == "no":
        print("✅")
        exit()
    else:
        print("Please enter either yes or no.")

garage = ["(1)  🏎", "(2)  🚌", "(3)  🚚", "(4)  🚐", "(5)  🚑", "(6)  🚒", "(7)  🚓", "️(8)  🚕",
          "(9)  🚗", "(10) 🚙", "(11) 🚛", "(12) 🛻", " "]
print("\nCars in garage: ")
for item in garage:
    print(item)


# Ask the user to choose a number and validate it
while True:
    try:
        chosen_car = int(input("Please choose your race car's number (from 1 to 12). Your choice: "))
        if 1 <= chosen_car <= 12:
            print(f"You have chosen car number {chosen_car}.")
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


print("\nStarting the race...")


cars = {1: "(1)  🏎",
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

# Sets up the starting positions for the cars
positions = {chosen_car: 0 for chosen_car in cars}


# Function to generate a random number
def rng():
    rand_num = random.randint(1, 12)
    print("Generating random number...\n"
          f"Number generated: {rand_num}. Car number {rand_num} will move forward one space.")


rng()


