import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Guess a number: "))
    
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")