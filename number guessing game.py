# number guessing game

# Version 1 - basic game

# 1 provide user with two inputs for the range of numbers to guess from
# 1.1 validate that the inputs are integers and that the lower end is less than the upper end
# 1.2 limit the range to a maximum of 100 to begin with
# 1.3 minimum range should be 10
# 1.4 verify range is valid before proceeding to the next step
# 1.5 verify that guessed number falls within the range of numbers to guess from

# 1.5 generate a random number from the range
# 1.6 ask user to guess the number
# 1.7 if the guess is correct, print a congratulatory message
# 1.8 if the guess is incorrect, print a message indicating whether the guess was too high or too low
# 1.9 for now, user can guess 5 times before the game is over


# Version 2
# 2.1 Add points system. User gets 1 point for each correct guess.
# 2.2 Add rounds. A game is 3-5 rounds long. 


# Version 3 - add GUI using tkinter



import random

print("Welcome to the Number Guessing Game!")

while True:
    try:
        low_end = int(input("Enter the lower end of the range: "))
        high_end = int(input("Enter the upper end of the range: "))
    except ValueError:
        print("Please enter valid integers for the chosen range.")
        continue

    if low_end >= high_end:
        print("Lower end cannot be higher than or equal to the upper end. Please enter a valid range.")
        continue

    # if high_end - low_end < 10:
    #     print("Minimum range is 10. Please enter a valid range.")
    #     continue

    if high_end - low_end > 100:
        print("Maximum range is 100. Please enter a valid range.")
        continue
    
    else:
        break

def number_guessing_game():
    random_number = random.randint(low_end, high_end)
    points = 0 # starting points
    round = 1 # starting round
    game_length = 3 # number of rounds in the game

    for game in range(game_length):
        guesses = 5 # number of guesses per round
        print(f"Round {round}: Guess the number between {low_end} and {high_end}. You have {guesses} guesses.")
        for n in range(guesses):
            if  guesses == 0:
                print(f"You've used all your guesses. The correct number was {random_number}. You've earned {points} points.")
                break

            guess = int(input("Guess the number: "))

            while True:
                if guess < low_end or guess > high_end: 
                    print(f"Please enter a number between {low_end} and {high_end}.")
                    guess = int(input("Guess the number: "))
                else:
                    break

            if guess == random_number:
                points += 1
                print(f"Congratulations! The correct number was {random_number}. You gained 1 point.")
                break
            elif guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            guesses -= 1

        if round > game_length:
            print(f"Congratulations! You've completed all rounds. You've earned {points} points.")
            break

number_guessing_game()

# kapd be a faszomxdd