print("Welcome to the temperature conversion app")

tf=float(input("\nWhat is the temperature in degree farenheit: "))
tf=round(tf,4)

tc=(tf-32)*5/9
tc=round(tc,4)

tk=tc+273.15
tk=round(tk,4)

print("\nDegree Farenheit:\t",tf)
print("Degree celcius:\t\t",tc)
print("Degree kelvin:\t\t",tk)
