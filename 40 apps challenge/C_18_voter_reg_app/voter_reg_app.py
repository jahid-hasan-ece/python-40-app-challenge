print("Welcome to Voter Register App")

#user information
name=input("\nPelase Enter your name: ").title().strip()
age=int(input("Please enter your age: "))

#politiacl parties info
parties=["Republican","Democratic","Independent","Libertarian","Green"]

if age<18:
    print("\nYou are not old enough to vote")
else:

    print("\nCongratulation "+name+"! you are old enough to register to vote.")

    print("\nHere is a list of political parties to join.")

    for party in parties:
        print("\t- "+party)

    choice=input("\nWhat party would you like to join: ").title().strip()
    

    if choice in parties:

        print("\nCongratulations "+name+"! you have joined the "+choice+" party")
    
        if choice=="Republican" or choice=="Democratic":
            print("This is a major party")
        
        elif choice=="Independent" or choice=="Libertarian":
            print("This is not a major party")
        else:
        
            print("This is not a popular  party at all")
    else:
        print("That is not a given party")
        

        
