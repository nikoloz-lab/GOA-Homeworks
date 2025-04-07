import random

def choose_secret_number():
    return random.randint(1, 10)  

def play_game():
    secret_number = choose_secret_number()
    guessed_correctly = False

    print("Welcome to the number guessing game!")
    print("Guess the secret number between 1 and 10.")

    while not guessed_correctly:
        guess = int(input("Your guess: "))
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the secret number!")
            guessed_correctly = True

play_game()