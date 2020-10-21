print("Welcome to the Favourite Teacher Program")

#user input
fav_teacher=[]

teacher_name=input("\nWho is your favourite teacher: ")
fav_teacher.append(teacher_name.title())
teacher_name=input("Who is your favourite teacher: ")
fav_teacher.append(teacher_name.title())
teacher_name=input("Who is your favourite teacher: ")
fav_teacher.append(teacher_name.title())
teacher_name=input("Who is your favourite teacher: ")
fav_teacher.append(teacher_name.title())

print("\nYour favourite teachers are: "+str(fav_teacher))
print("Your favourite teachers alphabetically are: " +str(sorted(fav_teacher)))
print("Your favourite teachers in reverse alphabetically order are: " +str(sorted(fav_teacher,reverse=True)))

print("\nYour top two favourite teachers are: "+fav_teacher[0]+" and "+fav_teacher[1])
print("Your next two favourite teachers are: "+fav_teacher[2]+" and "+fav_teacher[3])
print("Your last favourite teacher is: "+fav_teacher[-1])
print("You have a total of "+str(len(fav_teacher))+" faviourite teacher")

#add new first favourite teacher
new_teacher=input("\nOpps, "+fav_teacher[0]+" is no longer your first favourite teacher. Who is your new favourite teacher: ").title()
fav_teacher.insert(0,new_teacher)

#updated new fav_teacher list
print("\nYour favourite teachers ranked are: "+str(fav_teacher))
print("Your favourite teachers alphabetically are: " +str(sorted(fav_teacher)))
print("Your favourite teachers in reverse alphabetically order are: " +str(sorted(fav_teacher,reverse=True)))

print("\nYour top two favourite teachers are: "+fav_teacher[0]+" and "+fav_teacher[1])
print("Your next two favourite teachers are: "+fav_teacher[2]+" and "+fav_teacher[3])
print("Your last favourite teacher is: "+fav_teacher[-1])
print("You have a total of "+str(len(fav_teacher))+" faviourite teacher")

#teacher replace
rmv_teacher=input("\nYou have decided you no longer like a teacher. Which teacher =would you like to remove from your list: ").title()
fav_teacher.remove(rmv_teacher)

#updated new fav_teacher list
print("\nYour favourite teachers ranked are: "+str(fav_teacher))
print("Your favourite teachers alphabetically are: " +str(sorted(fav_teacher)))
print("Your favourite teachers in reverse alphabetically order are: " +str(sorted(fav_teacher,reverse=True)))

print("\nYour top two favourite teachers are: "+fav_teacher[0]+" and "+fav_teacher[1])
print("Your next two favourite teachers are: "+fav_teacher[2]+" and "+fav_teacher[3])
print("Your last favourite teacher is: "+fav_teacher[-1])
print("You have a total of "+str(len(fav_teacher))+" faviourite teacher")



