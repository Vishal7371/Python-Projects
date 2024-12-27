import random
# Computer choice 
def my_coumputer_choice():
    choices =["Rock","Paper","Scissor"]
    return random.choice(choices)
# User Choice 
def my_choice():
    print("Welcome to the  game !!!!!")
    print ("1. Rock")
    print ("2. Paper")
    print ("3. Scissor")
    choice = int(input("What do you want to choose 🙄"))
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissor"
    else:
        print("Invalid Choice !! Please Try Again")
        return my_choice()
# Determining the winner
def determin_winner(user,computer):
    if user == computer:
        return "It's a tie"
    elif (user == "Rock" and computer == "Scissor") or \
         (user == "Scissor" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
            return "You Win" 
    else:
        return "Computer Win"
def play_game():
    print("Welcome to Rock, Paper, Scissor game!!")
    while True:
        user_choice=my_choice()
        computer_choice=my_coumputer_choice()
        print(f"You choose:{user_choice}")
        print(f"Computer choose:{computer_choice}")
        result=determin_winner(user_choice,computer_choice)
        print(result)
        play_again = input("\nDo you want to play again? (y/n)")
        if play_again.lower() != 'y':
            print("Thanks for playing! GoodBye!")
            break
   
if __name__ == "__main__":
    play_game()

    

    
    

    


    


