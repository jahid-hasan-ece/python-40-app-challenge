import math
print("Welcome to the right triangle solver app")

leg1=float(input("\nwhat is the first leg of the trangle: "))
leg2=float(input("what is the second leg of the trangle: "))

#calculation
hypontenus=math.sqrt(leg1**2+leg2**2)
area=.5*leg1*leg2

#round figure
hypontenus=round(hypontenus,3)
area=round(area,3)

print("\nFor a triangle with legs of "+ str(leg1)+" and "+str(leg2)+ " the hypontenus is " +str(hypontenus))
print("For a triangle with legs of "+ str(leg1)+" and "+str(leg2)+ " the area is " +str(area))


