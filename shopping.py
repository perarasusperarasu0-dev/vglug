
# _______________________________________________________________________________________________________
#                        SHOPPING CART USING LOOP STATEMENT    
# _______________________________________________________________________________________________________
total_amt= 0

for i in range(5):
     purchase_price = int(input("ENTER THE PRICE OF ITEM : $ "))
     total_amt = total_amt + purchase_price

print("TOTAL PURCHASE AMOUNT IS : $", total_amt)

