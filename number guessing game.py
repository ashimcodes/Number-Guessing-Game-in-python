import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Enter your guess (1-100): "))
        attempts += 1
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"You got it in {attempts} attempts! The number was {number}.")
            break

if __name__ == "__main__":
    print("Welcome to the number guessing game!")
    play_game()
    play_again = input("Would you like to play again? (yes/no) ")
    while play_again == "yes":
        play_game()
        play_again = input("Would you like to play again? (yes/no) ")
    print("Thanks for playing! Have a great day.")
