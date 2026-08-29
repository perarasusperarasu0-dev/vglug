customer_ID = int(input("Enter the Customer ID:"))
customer_name = str(input("Enter your Customer name: "))
unit = int(input("Enter your unit:"))
type = str(input("Enter the type(commercial or non-commercial):"))

# ------------------commercial type--------------------

if unit>=100 and unit<=200 and type=="commercial":
     print("your Bill amount is NO amount")
elif unit>=200 and unit<=400 and type=="commercial":
     print("your Bill amount is ",unit*4)
elif unit>=500 and unit<=600 and type=="commercial":
     print("your Bill amount is ",unit*6)

# ------------------non-commercial type--------------------

if unit>=100 and unit<=200 and type=="non-commercial":
     print("your Bill amount is NO amount") 
elif unit>=200 and unit<=400 and type=="non-commercial":
     print("your Bill amount is ",unit*2)
elif unit>=500 and unit<=600 and type=="non-commercial":
        print("your Bill amount is ",unit*3)
else:
        print("invalid input")