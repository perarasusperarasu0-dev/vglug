balance = 5000
while balance > 0:
    print("YOUR CURRENT BALANCE IS: $", balance)
    withdrawal_amount = int(input("ENTER THE AMOUNT TO WITHDRAW: $ "))
    if withdrawal_amount <= balance:
        balance = balance - withdrawal_amount
        print("WITHDRAWAL SUCCESSFUL")
        print("YOUR UPDATED BALANCE IS: $", balance)
    else:
        print("INSUFFICIENT FUNDS")
print("YOUR FINAL BALANCE IS: $", balance)