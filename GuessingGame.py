#gaussing game
#secret_number = 10
#geuss_count = 0
#maximum_trials = 3

#while geuss_count < maximum_trials:
 #   number = int(input("guess a number: "))
  #  if number != secret_number:
   #     print("sorry try again")
    #    geuss_count += 1
     #   continue
    #else:
     #   print(f" Congradulations, the secret number is : {secret_number}!")
      #  break
#else:
 #   print("FAILED")
#PUT IT IN A CLASS
class Game:
    pass
    def geussing_game():
        secret_number = 10
        geuss_count = 0
        maximum_trials = 3
        while geuss_count < maximum_trials:
            number = int(input("guess a number: "))
            if number != secret_number:
                print("sorry try again")
                geuss_count += 1
                continue
            else:
                print(f" Congradulations, the secret number is : {secret_number}!")
                break
        else:
            print("FAILED")

    geussing_game()






