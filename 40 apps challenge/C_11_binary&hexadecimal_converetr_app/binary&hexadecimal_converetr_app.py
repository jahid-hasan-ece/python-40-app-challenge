print("Welcome to the Binary/Hexadecimal converter app")

#how many numbers user want to convert &converting process end
binary=[]
hexa=[]

limit=int(input("\nCompute the binary headecimal values upto the following decimal number: "))
for value in range(1,limit+1):
    binary.append(bin(value))
    hexa.append(hex(value))

print("Generating lists....complete!")

print("\nUsing slice, we will show a portion of each list.")
start_num=int(input("What decimal number would you like to start at: "))
end_num=int(input("What decimal number would you like to stop at: "))

#slicing the list items

print("\nDecimal values from " + str(start_num)+ " to " +str(end_num))
for values in range(start_num,end_num+1):
    print(values)

print("\nBinary values from " + str(start_num)+ " to " +str(end_num))
for values in binary[start_num-1:end_num]:
      print(values)
  
print("\nHexadeimal values from " + str(start_num)+ " to " +str(end_num))
for values in hexa[start_num-1:end_num]:
      print(values)
                

#click enter to see the full convert list upto the limit

input("\npress enter to see all values from 1 to "+str(limit))
print("Decimal....Binary....Hexadecimal")
print(".............................................")

for value in range(1,limit+1):
    print(str( value)+"...."+str(binary[value-1])+"...."+str(hexa[value-1]))
     
      
