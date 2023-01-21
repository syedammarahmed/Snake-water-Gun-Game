#Making Snake,Water,Gun Game
#Using random librarie
import random
list = ["Snake","Water","Gun"]
choice = random.choice(list)
print("U have only 5 chhance")
Chance = 6
chance = 5
no_of_chance=0
#using while loop to repeat only as par chaces
while(chance<=5):
      for i in range(Chance-1):
            print("\nChoose Option\n"
                  "Snake : S\n"
                  "Water : W\n"
                  "Gun   : G\n")
            user_choice = input("Its Your chance to choose : ").capitalize()
            #print("Chance left now",i)
            if choice=="Snake" and user_choice=="S":
                  print("You r tie the Game")
            elif choice=="Snake" and user_choice=="W":
                  print("You Loss the Game")
            elif choice=="Snake" and user_choice=="G":
                  print("You win the Game")
            if choice=="Water" and user_choice=="W":
                  print("You r tie the Game")
            elif choice=="Water" and user_choice=="G":
                  print("You Loss the Game")
            elif choice=="Water" and user_choice=="S":
                  print("You win the Game")
            if choice=="Gun" and user_choice=="G":
                  print("You r tie the Game")
            elif choice=="Gun" and user_choice=="S":
                  print("You Loss the Game")
            elif choice=="Gun" and user_choice=="W":
                  print("You win the Game")
            elif user_choice!="G"and user_choice!="W" and user_choice!="S":
                  print("Your option is wrong")
                  print("Please Check Your Option")
            else:
                  no_of_chance=no_of_chance+1
                  print(f"{Chance-no_of_chance} out of {chance} chance is remaining")
      break
print("\nYour chance is finish")
print("Game Over")


