import random

def check_winner(player_choice, computer_choice):
    # Determine the winner based on the rules
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "snake" and computer_choice == "water") or \
         (player_choice == "water" and computer_choice == "gun") or \
         (player_choice == "gun" and computer_choice == "snake"):
        return "You win!"
    else:
        return "Computer wins!"

def get_computer_choice():
    # Randomly select the computer's choice
    return random.choice(["snake", "water", "gun"])

def main():
    print("Welcome to Snake, Water, Gun Game!")
    print("Choices: snake, water, gun")
    
    player_choice = input("Enter your choice (snake/water/gun): ").lower()
    
    if player_choice not in ["snake", "water", "gun"]:
        print("Invalid choice! Please enter snake, water, or gun.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    result = check_winner(player_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
    
    
    
    
    
    
# import random

# def check(comp, user):
#   if comp ==user:
#     return 0
    
#   if(comp == 0 and user ==1):
#     return -1
    
#   if(comp == 1 and user ==2):
#     return -1
    
#   if(comp == 2 and user == 0):
#     return -1

#   return 1
    
  
# comp = random.randint(0, 2)
# user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

# score = check(comp, user)

# print("You: ", user)
# print("Computer: ", comp)

# if(score == 0):
#   print("Its a draw")
# elif (score == -1):
#   print("You Lose")
# else:
#   print("You Won")
  
  
