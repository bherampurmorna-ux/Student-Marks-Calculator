import random

number = random.randint(1, 10)
attempts = 0
print("Guess the number between 1 and 10")

while True:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

    if guess == number:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")