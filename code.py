import random
print("Number gussing game")
number-random.randint(1,0)
chances-0
print("Guess == number(between 1 and 9):")

while chances < 5:

    guess = int(input("Enter your guess:- "))

    if guess == number:
        print("Congratulation YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: guess a number higher than", guess)

    else:
        print("Your guess was too high: guess a number lower than", guess)

    chances +=1

if not chances <5:
    print("YOU LOSE!!! the number is", number)
    





