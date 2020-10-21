import random
print("Welcome to the guess my number app.")

#user info
name=input("\nHwllo! What is your name: ")
print("Well "+name+", I am thinking of a number between 1 to 20.")

#guessing number by user
number=random.randint(1,20)

for num in range(5):
    
    guess=int(input("\nTake a guess: "))

    if guess==number:
        print("\nGood job, "+name+"! You guessed my num in "+str(num+1)+" guesses")
        break
    else:
        if guess<number:
            print("Your guess is too low")

        elif guess>number:
            print("Your guess is too high")
            
    if num==4:
        print("\nGame Over. The number I was thinking of was "+str(number))
            
        



