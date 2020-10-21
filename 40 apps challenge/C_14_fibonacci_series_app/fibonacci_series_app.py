print("Welcome to the Fibonacci Calculator app")

#user input for fibonacci series and calculation

digits=int(input("\nHow many digits of the Fibonacci sequence would you like to compute: "))

lst=[]
digit_1=0
digit_2=1
for digit in range(digits):
    result=digit_1+digit_2
    digit_2=digit_1
    digit_1=result
    print(result)
    lst.append(result)
  

#golden ratio
print("\nThe golden ratio values are: ")
   
for num in range(len(lst)-1):
    print(lst[num+1]/lst[num])

print("\nThe ratio of consecutive fibonacci terms approches phi: 1.618.....")

           
      
