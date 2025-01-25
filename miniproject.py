import random

# Mapping user input to numbers
youdict = {"s": 1, "w": -1, "g": 0}
reversdict = {1: "Snake", -1: "Water", 0: "Gun"}

# Computer's random choice (fixed)
computer = random.choice([1, -1, 0])

# Get user input
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Validate input
if youstr not in youdict:
    print("Invalid input! Please choose 's', 'w', or 'g'.")
else:
    # Map user choice
    you = youdict[youstr]

    # Display choices
    print(f"You chose {reversdict[you]}")
    print(f"Computer chose {reversdict[computer]}")

    # Determine the result
    if computer == you:
        print("It's a draw!")
    elif (you - computer) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")
