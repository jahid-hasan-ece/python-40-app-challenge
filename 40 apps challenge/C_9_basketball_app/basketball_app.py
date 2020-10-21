print("Welcome to the basketball roster app")

#user input
player=[]

player_position=input("\nWho is your point guard: ")
player.append(player_position.title())
player_position=input("Who is your shooting guard: ")
player.append(player_position.title())
player_position=input("Who is your small forward: ")
player.append(player_position.title())
player_position=input("Who is your power forward: ")
player.append(player_position.title())
player_position=input("Who is your center: ")
player.append(player_position.title())

#player list
print("\n\tYour starting " + str(len(player)) + " for the upcoming basketball season")
print("\t\tPoint Guard:"+"\t\t"+ player[0])
print("\t\tShooting Guard:"+"\t\t"+ player[1])
print("\t\tSmall Forward:"+"\t\t"+ player[2])
print("\t\tPower forward:"+"\t\t"+ player[3])
print("\t\tCenter:"+"\t\t\t"+ player[4])

#injured players and add new player
injured_player=player.pop(2)
print("\nOh no, "+injured_player+ " is injured.")
print("Your roster is only has "+str(len(player))+" players.")
new_player=input("Who will take "+injured_player+"'s spot: ").title()
player.insert(2,new_player)


#update player list
print("\n\tYour starting " + str(len(player)) + " for the upcoming basketball season")
print("\t\tPoint Guard:"+"\t\t"+ player[0])
print("\t\tShooting Guard:"+"\t\t"+ player[1])
print("\t\tSmall Forward:"+"\t\t"+ player[2])
print("\t\tPower forward:"+"\t\t"+ player[3])
print("\t\tCenter:"+"\t\t\t"+ player[4])

print("\nGood luck "+new_player+", you will do great!")
print("Your roster has now "+str(len(player))+ " players.")

