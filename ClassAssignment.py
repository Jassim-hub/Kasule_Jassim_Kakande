Account_Balance = int(input("Enter amount to deposit: "))
print("Choose an option:")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        deposit = int(input("Enter amount to deposit: "))
        Account_Balance += deposit
        print("Amount Deposited:", deposit)
        print("New Balance:", Account_Balance)
    elif choice == 2:
        withdraw = int(input("Enter amount to withdraw: "))
        if Account_Balance >= withdraw:
            Account_Balance -= withdraw
            print("Amount Withdrawn:", withdraw)
            print("New Balance:", Account_Balance)
        else:
            print("Insufficient balance")
    elif choice == 3:
        print("Account Balance:", Account_Balance)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
