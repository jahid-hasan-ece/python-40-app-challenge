print("\t\t\tSummary Table")

#str list
num_string=["15","100","55", "42"]
print("\nThe variable num_string is a ",type(num_string))
print("It contains the element: ",num_string)
print("The element",num_string[0],"is a",type(num_string[0]))

#int list
num_int=[15,100,55, 42]
print("\nThe variable num_int is a ",type(num_int))
print("It contains the element: ",num_int)
print("The element",num_int[0],"is a",type(num_int[0]))

#float list
num_float=[15.5,100.0,5.0, 42.2765]
print("\nThe variable num_float is a ",type(num_float))
print("It contains the element: ",num_float)
print("The element",num_float[0],"is a",type(num_float[0]))

#str list
num_list=[[1,2,3],[4,5,6],[7,8,9]]
print("\nThe variable num_list is a ",type(num_list))
print("It contains the element: ",num_list)
print("The element",num_list[0],"is a",type(num_list[0]))

#sorting
print("\nNow sorting num_strings and num_ints...")
num_string.sort()
num_int.sort()
print("Sorted num_string:",num_string)
print("Sorted num_int:",num_int)

print("\nStrings are sorted alphabetically while integer are sortednumerically")

