pin = 1234
balance = 1000
if pin == 1234:
    print("Welcome to the ATM!")
    print("Your current balance is: $", balance)
    withdrawal_amount = float(input("Enter the amount to withdraw: "))
    
    if withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print("Withdrawal successful!")
        print("Your new balance is: $", balance)
    else:
        print("Insufficient funds. Transaction canceled.")  
        