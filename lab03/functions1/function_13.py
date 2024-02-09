import random

def guess_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    target = random.randint(1, 20)
    guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1
        if guess < target:
            print("Your guess is too low.")
        elif guess > target:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses.")
            break

guess_number()
