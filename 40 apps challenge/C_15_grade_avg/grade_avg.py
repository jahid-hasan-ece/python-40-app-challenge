print("Welcome to the Grade average calculator app")

#user input grade number

name=input("\nWhat is your name: ")
sub_num=int(input("How many grades would you like to enter: "))

grades=[]
for i in range(sub_num):
    grade_num=int(input("Enter grade: "))
    grades.append(grade_num)

#sorting & other details
grades.sort(reverse=True)

print("\nGrades highest to lowest: ")
    
for grade in grades:
    print("\t"+str(grade))

print("\nMikes grade summary:")

print("\tTotal numbers of grades: "+str(sub_num))
print("\tHighest grade: "+str(max(grades)))
print("\tlowest grade: "+str(min(grades)))
avg=sum(grades)/sub_num
print("\tAverage: "+ str(avg))


#expected avg with next assignment value
exp_avg=int(input("\nWhat is your expected average: "))

print("\nGood luck "+name)
asgn_num=exp_avg*(sub_num+1)-sum(grades)
print("You will need to get "+str(asgn_num)+" on your next assignment to earn a "+str(exp_avg)+" average.")

#copy the list and change the grade
print("\nLets see what your average could have been if you did better/worse in assignment.")
old_grade=int(input("What wopuld you like to change: "))
new_grade=int(input("What wopuld you like to change "+str(old_grade)+" to: "))

new_grades=grades.copy()
new_grades.remove(old_grade)
new_grades.append(new_grade)
new_grades.sort(reverse=True)

#showing new grades and diffeence between to avg of grades with original grades

print("\nNew grades highest to lowest:")
for i in new_grades:
    print("\t",i)
print("\nMike's new grades summary:")
print("\tTotal numbers of grades: "+str(sub_num))
print("\tHighest grade: "+str(max(new_grades)))
print("\tlowest grade: "+str(min(new_grades)))
new_avg=sum(new_grades)/sub_num
print("\tAverage: "+ str(new_avg))

print("\nYour new average would be a "+str(sum(new_grades)/sub_num)+" comapre to your real averafe of "+str(sum(grades)/sub_num))
print("This is a change of "+ str(round(new_avg-avg,1))+" points!")

print("\nToo bad your original grades are still the same!")
print(grades)
print("You should go ask for extra credit")

