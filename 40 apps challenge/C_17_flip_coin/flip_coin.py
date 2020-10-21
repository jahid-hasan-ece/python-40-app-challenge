import random

print("Welcome to the coin toss app")

#user input no. of flips
print("\nI will flip a coin a set number of times.")
flip_number=int(input("How many times would you like me to flip the coin: "))
choice=input("Would you like to see the result of each flip (y/n): ").lower()

Head=0
Tail=0

for flip in range(flip_number):
    coin=random.randint(0,1)
    if coin==0:
        Head+=1
        if choice.startswith("y"):
            print("Heads")
    else:
        Tail+=1
        if choice.startswith("y"):
            print("Tails")

    #Special message
    if Head==Tail:
        print("At "+ str(flip+1)+" flips, the number of heads and tails were equal at "+str((flip+1)/2)+" each")

#percentage calculation
print("\nResults of Flipping A Coin "+str(flip_number)+" Times:")

print("\nSide\t\tCount\t\tPercentage")
H_percentage=(Head/flip_number)*100
T_percentage=(Tail/flip_number)*100

print("Heads\t\t"+str(Head)+"/"+str(flip_number)+"\t\t"+str(round(H_percentage,2)))
      
print("Tails\t\t"+str(Tail)+"/"+str(flip_number)+"\t\t"+str(round(T_percentage,2)))

              
        
             
            
                            
                        
                
