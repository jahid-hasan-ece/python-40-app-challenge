print("Welcome to Grade sorter App")

#create a null list
grade=[]

#user input
first_grade=int(input("\nWhat is yur first grade(0-100) : "))
grade.append(first_grade)

second_grade=int(input("What is yur second grade(0-100) : "))
grade.append(second_grade)

third_grade=int(input("What is yur third grade(0-100) : "))
grade.append(third_grade)

fourth_grade=int(input("What is yur fourth grade(0-100) : "))
grade.append(fourth_grade)

print("\nYour Grades are: " + str(grade))

#sorting
grade.sort(reverse=True)

print("\nYour grades are highest to lowest: ",grade)

#pop 2 lowest grade
print("\nThe lowest two grades will now be dropped.")

r1=grade.pop()
print("removed grade: "+ str(r1))

r2=grade.pop()
print("removed grade: "+ str(r2))

#remaining & highest
print("\nYour remaining grade: " + str(grade))


print("Nice work! Your highest grade is ",grade[0])



