import random

computer_wins = 0
user_wins = 0

def user_winner():
    print("You win this round!")

def computer_winner():
    print("You lose this round.")

def draw_round():
    print("Both options are the same.")

def round_summary(usr, comp):
    print("\nRound summary")
    print(f"User wins: {usr}\nComputer wins: {comp}")

print("----------Welcome to the Snake Water Gun game!----------")   #S=0, W=1, G=2

while True:
    print("\nGame choices:")
    print("1.Play")
    print("2.Quit")
    option = input("Choose an option: ")

    match option:
        case "1":
            user_input = input("\nEnter a number (S:0, W:1, G:2): ")
            computer_input = random.randint(0,2)
            print(f"Computer chooses {computer_input}.")
            match user_input:
                case "0":
                    if computer_input==1: 
                        user_wins+=1
                        user_winner()
                    elif computer_input==2: 
                        computer_wins+=1
                        computer_winner()
                    else: draw_round()
                case "1":
                    if computer_input==0: 
                        computer_wins+=1
                        computer_winner()
                    elif computer_input==2: 
                        user_wins+=1
                        user_winner()
                    else: draw_round()
                case "2":
                    if computer_input==0: 
                        user_wins+=1
                        user_winner()
                    elif computer_input==1: 
                        computer_wins+=1
                        computer_winner()
                    else: draw_round()
                case _: print("Invalid input!")
        case "2":
            print(f"\n----------Final scores----------")
            print(f"You win {user_wins} rounds.\nComputer wins {computer_wins} rounds")
            if user_wins>computer_wins: print("YOU WIN!!!")
            elif computer_wins>user_wins: print("You lose.")
            else: print("It's a draw.")
            break
        case _:
            print("Invalid input")
        
    round_summary(user_wins, computer_wins)