print("Welcome to the shipping account program")

#user account create and shipping information

account_holder=['davis','moris','ozil','ronaldo']

username=input("\nHello, What is your username: ").lower().strip()

for name in account_holder:
    if name!=username:
        if name==account_holder[-1]:
            print("\nSorry, you do not have an account with us. Goodbye.")
            
        continue
    else:
        print("\nHello "+name+". Welcome back to your account.")
        print("Current shipping prices are as follows: ")

        print("\nShipping orders 0 to 100:\t\t$5.10 each")
        print("Shipping orders 100 to 500:\t\t$5.00 each")
        print("Shipping orders 500 to 1000:\t\t$4.95 each")
        print("Shipping orders over 1000:\t\t$4.80 each")

        item=int(input("\nHow many items would you like to ship: "))
        
        if item<=100:
            price=item*5.10
            print("To ship this items it will cost you $"+str(round(price,2))+" at $5.10 per item.")
            order_confirm=input("\nWould you like to place this order (y/n): ").lower()
            if order_confirm.startswith("y"):
                print("Okay. Shipping your "+str(item)+" items.")
                break
                    
            else:
                print("Okay. No order is being placed at this time")
                break
            
        elif item<=500:
            price=item*5.00
            print("To ship this items it will cost you $"+str(round(price,2))+" at $5.00 per item.")
            order_confirm=input("\nWould you like to place this order (y/n): ").lower()
            if order_confirm.startswith("y"):
                print("Okay. Shipping your "+str(item)+" items.")
                break
            else:
                print("Okay. No order is being placed at this time")
                break
                
        elif item<=1000:
            price=item*4.95
            print("To ship this items it will cost you $"+str(round(price,2))+" at $4.95 per item.")
            order_confirm=input("\nWould you like to place this order (y/n): ").lower()
            if order_confirm.startswith("y"):
                print("Okay. Shipping your "+str(item)+" items.")
                break
            else:
                print("Okay. No order is being placed at this time")
                break
                
        else:
            price=item*4.80
            print("To ship this items it will cost you $"+str(round(price,2))+" at $4.80 per item.")
            order_confirm=input("\nWould you like to place this order (y/n): ").lower()
            if order_confirm.startswith("y"):
                print("Okay. Shipping your "+str(item)+" items.")
                break
            else:
                print("Okay. No order is being placed at this time")
                break
    
           
                 
       

