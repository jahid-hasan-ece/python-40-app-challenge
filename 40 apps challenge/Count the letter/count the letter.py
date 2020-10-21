print("Welcome to the letter counter app")
print("")
name=input("what is your name: ")
print("Hello "+ name+ "!")
print("i will count the number of times that a specific letters occurs in a message\n")

message=input("please enter a message: ")
count_letter=input("Which letter you want to count : ")
message=message.lower()
result=message.count(count_letter)
print(result)

