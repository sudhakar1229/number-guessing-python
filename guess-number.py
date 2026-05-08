import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess Number: "))

    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct!")
        break