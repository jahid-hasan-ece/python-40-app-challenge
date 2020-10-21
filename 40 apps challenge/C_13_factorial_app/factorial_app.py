import math
print("Welcome to the Factorial App")

#calculating factorial using function

num=int(input("\nWhich value you want to enter for factorial?: "))

print(str(num)+ "! = ",end="" )
for value in range(1,num+1):
    print(str(value) + "*" , end="")

fact=math.factorial(num)
print("\n\nThe math library value of the factorial of the number: "+str(fact))

#manual algorithom
fact=1
for value in range(1,num+1):
    fact*=value

print("\nthe own algorithm value of the factorial of the number: "+str(fact))

#double of the factorial
print("\nthe 2nd times of the factorial is "+str(fact**2))
