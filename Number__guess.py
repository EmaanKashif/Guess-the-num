# import random

# def Guess_num():
#         print("Welcome to the number guessing game!")
#         random_num = random.randint(1,100)
#         for i in range(5):
#             guess = int(input("Guess the number and I will give u hint if number is too high or low: "))
#             if guess == random_num:
#               print("Yahoo! You guess it right")
#             elif guess > random_num:
#                print("Number is higher")
#             elif guess < random_num:
#                print("Number is lower")
#             else:
#                print("Enter a valid number")

# Guess_num()

import random

def guess_num():
    print("Welcome to the number guessing game!")
    
    while True:  # Loop to allow for replaying the game
        random_num = random.randint(1, 100)
        attempts_left = 5
        
        while attempts_left > 0:
            guess = int(input("Guess the number (1-100): "))
            
            if guess == random_num:
                print("Yahoo! You guessed it right.")
                break
            elif guess < random_num:
                print("The number is lower.")
            elif guess > random_num:
                print("The number is higher.")
            
            attempts_left -= 1
            if attempts_left > 0:
                print(f"You have {attempts_left} guess(es) left.")
            else:
                print(f"Sorry, you're out of guesses. The number was {random_num}.")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

guess_num()
