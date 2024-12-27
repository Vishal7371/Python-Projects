import random
number_guess=random.randint(1,100)
while True:
    user_guess=int(input("Guess the number between 1 to 100:"))
    if user_guess < number_guess:
        print("Too low! Try again.")
    elif user_guess > number_guess:
        print("Too High! Try Again.")
    else:
        print("Congratulations! You have won the game")
        break
a

