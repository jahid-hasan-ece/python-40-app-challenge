import math
import cmath

print("Welcome to the Quadratic Solver App")


print("\nA Quadratic equation is of the form ax^2 + bx + c")
print("Your solution can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real number and bj is the imaginary portion")

#user input for how many equation solve

eqn_num=int(input("\nHow many equations would you like to solve today: "))


#user input coefficient values for equations


for eqn in range(1,eqn_num+1):
    
    print("\nSolving equation #"+str(eqn))
    print("........................................")
    
    a=float(input("\nPlease enter your value of a (coefficient of x^2): "))
    b=float(input("\nPlease enter your value of b(coefficient of x): "))
    c=float(input("\nPlease enter your value of c (coefficient): "))
    d=cmath.sqrt(b**2-4*a*c)
    x1=complex((-b+d)/2*a)
    x2=complex((-b-d)/2*a)
    print("\nThe solution to " + str(a)+"x^2 + "+str(b)+ "x + " + str(c) +" = 0 are :")
    print("\n\tx1 = " +str(x1))
    print("\n\tx2 = " +str(x2))

print("\nThank you for using the Quadratic solver app. Goodbye.")
    
     
