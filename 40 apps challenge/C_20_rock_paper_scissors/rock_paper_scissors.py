import random
print("Welcome to a game of Rock Paper Scissors")

#round of games
steps=int(input("\nHow many rounds you want to play: "))
game=["rock","paper","scissors"]

player=0
computer=0

for step in range(1,steps+1):
    print("\nRound"+ str(step))
    print("player: "+str(player)+"\tComputer: "+str(computer))
    my_choice=input("Time to pick....rock, paper, scissors: ").lower().strip()
    
    comp_choice=random.choice(game)
    print("\tComputer: "+comp_choice)
    print("\tPlayer: "+my_choice)

    if my_choice  not in game:
        print("\tthat is not a valid game option!")
        print("\tComputer gets the point!")
        computer+=1

    elif comp_choice==my_choice:
        print("\tIt is a tie, how boring")
        print("\tThis round was a tie")

    #my win condition
    
    elif comp_choice=="rock" and my_choice=="paper":
        print("\tPaper covers rock")
        print("\tyou win round "+str(step))
        player+=1
        
    elif comp_choice=="paper" and my_choice=="scissors":
        print("\tscissors cuts paper")
        print("\tyou win round "+str(step))
        player+=1

    elif comp_choice=="scissors" and my_choice=="rock":
        print("\trock breaks scissors")
        print("\tyou win round "+str(step))
        player+=1

        #computer win condition
      
    elif comp_choice=="paper" and my_choice=="rock":
        print("\tPaper covers rock")
        print("\tComputer wins round "+str(step))
        computer+=1
        
    elif comp_choice=="scissors" and my_choice=="paper":
        print("\tscissors cuts paper")
        print("\tComputer wins round "+str(step))
        computer+=1

    elif comp_choice=="rock" and my_choice=="scissors":
        print("\trock breaks scissors")
        print("\tComputer wins round "+str(step))
        computer+=1

#final result
print("\nFinal Game results")

print("\tRounds played "+str(steps))
print("\tplayer Score: "+str(player))
print("\tComputer Score: "+str(computer))

#winer declare
if player>computer:
    print("\tWinner: Player :-(")
elif computer>player:
    print("\tWinner: Computer :-(")
else:
    print("\tthe game was a tie")

        
