name = input("Type your name:")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go either left or right. Which way would you like to go? ").lower()

if answer == "left":
   answer = input("You've come to a river, you can walk around it or swim across Type walk to walk around or swim to swim across: ")
   if answer == "swim":
      print("You swam across and were eaten by an aligator and lost the game!")
   elif answer == "walk": 
       print("You walked for many miles, ran out of water and lost the game!")
   else:
        print("Not a valid choice. You loose!")

elif answer == "right":
    answer = input("You've come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
          print("You got back and lost!!")
    elif answer == "cross": 
         answer = input("You've crossed the bridge and met a. Do you talk to them (yes/no)? ")
         if answer == "yes":
           print("The stranger gave you a golden tickect. You Won!")
         elif answer == "no":
           print("You ignored the stranger and lost!")
         else:
            print("Not a valid choice. You loose!")
      
    else:
        print("Not a valid choice. You loose!")

else:
    print("Not a valid choice. You loose!")

print("Thank you for participating", name + "!")