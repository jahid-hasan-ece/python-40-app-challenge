#create a datetime object and shoeing the current date and time
import datetime
print("Welcome to the grocery list app")

x = datetime.datetime.now()

print("Current date and time:",x.strftime("%m/%d"),"\t",x.strftime("%H:%M"))

#create list
item=["Meat","Cheese"]

print("You currently have "+ item[0] + " and "+ item[1] +" in your list.")

#add new food item

new_item=input("\nType of food to add to the grocery list: ")
item.append(new_item.title())
new_item=input("Type of food to add to the grocery list: ")
item.append(new_item.title())
new_item=input("Type of food to add to the grocery list: ")
item.append(new_item.title())
print("Here is your grocery list:")
print(item)

#sorting list
item.sort()
print("\nHere is your grocery list sorted:")
print(item)

#simulation shop cart

print("\nSimulating grocerry shopping....")

item_len=len(item)
print("\nCurrent grocery list: "+str(item_len)+" items")
print(item)

#buying item being deleted

buy_item=input("What food did you just buy: ").title()
item.remove(buy_item)
print("Removing "+ buy_item+ " from the list...")


item_len=len(item)
print("\nCurrent grocery list: "+str(item_len)+" items")
print(item)

buy_item=input("What food did you just buy: ").title()
item.remove(buy_item)
print("Removing "+ buy_item+ " from the list...")

item_len=len(item)
print("\nCurrent grocery list: "+str(item_len)+" items")
print(item)

buy_item=input("What food did you just buy: ").title()
item.remove(buy_item)
print("Removing "+ buy_item+ " from the list...")

item_len=len(item)
print("\nCurrent grocery list: "+str(item_len)+" items")
print(item)

#Items are out of range.so exchange items
no_item=item.pop()
print("\nSorry, the store is out of "+ no_item + ".")
new_item=input("What food would you like to instead: ").title()

item.insert(0,new_item)

print("\nHere is what remains in your grocery list: ")
print(item)



