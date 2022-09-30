#generate a random number
# track how many times the user takes to guess it
import random
top_of_range = input("enter highest number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print ("enter a number greater than zero") 
        quit()
else:
    print(" enter a digit number")
    quit()
random_number = random.randint(0, 10)
guess = 0 
while True: # random number == guess
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print(" enter a digit number: ")
        continue
    if user_guess == random_number:
        print("you got it! the number is", random_number," !!")
        break

    elif user_guess > random_number:
        print(" The number is above the target number")
    else:
        print(" your are below the target")

print(" You got it in", guess, "guesses")





