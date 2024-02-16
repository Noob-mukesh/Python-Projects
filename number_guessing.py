# Number Guessing Game Using python..
import random
def play_guessing_game():
    print("Welcome to the Guessing Game!")
    #  by @mr_sukkun 
    # join  : https://t.me/Python_Codes_Pro
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the secret number {secret_number} in {attempts} attempts!")
            break
play_guessing_game()
