input1 = int(input("Please enter your max number: "))
import random
random1 = random.randint(0,input1)
answer1 = int(input("Please guess a number betweem 0 and "+ str(input1) + ": " ))
while (answer1 != random1):
    print(answer1)
    if (answer1 < random1):
        print("You're too low.")
        answer1 = int(input("Please guess again: "))
    elif (answer1 > random1):
        print("You're too high.")
        answer1 = int(input("Please guess again: "))
    else:
        print("Error! Please guess a number!")
        answer1 = int(input("Please guess again: "))
    print("Congrats! You Win!")