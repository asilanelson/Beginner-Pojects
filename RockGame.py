import random
#rock,scissors and paper
user_wins = 0
computer_wins = 0
options = ["rock", "scissors", "paper"]

while True:
    user_input = input("Type rock/scissors/paper or Quit(q):  " ).lower()
    if user_input == "q":
        break
    if user_input not in ("rock", "scissors", "paper"):
        print(" not applicable, enter a valid choice ")
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number] 
    print("computer picked " , computer_pick, ".")
    if user_input == "rock" and computer_pick == "scissors":
        print("YOU WON!")
        user_wins += 1
         
    elif user_input == "paper" and computer_pick == "rock":
        print("YOU WON!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("YOU WON!")
        user_wins += 1
    else:
        print("YOU LOST")
        computer_wins +=1

print("You won" ,user_wins, "times !")
print("computer won",computer_wins, "times !")
print(" sad to see you leave")





