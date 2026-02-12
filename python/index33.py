# Python Program Banking

def show_balance(balance):
    print("**************************")
    print(f"Your balance is ${balance:.2f}")
    print("**************************")

def deposit():
    try:
        amount = float(input("Enter the amount to be deposited: "))
    except ValueError:
        print("Invalid amount entered.")
        print("**************************")
        return 0.0

    if amount < 0:
        print("That is not a valid amount")
        print("**************************")
        return 0.0
    else:
        return amount

def withdraw(balance):
    try:
        amount = float(input("Enter the amount to be withdrawn: "))
    except ValueError:
        print("Invalid amount entered.")
        print("**************************")
        return 0.0

    if amount > balance:
        print("Insufficient Balance")
        print("**************************")
        return 0.0
    elif amount < 0:
        print("Amount must be greater than 0")
        print("**************************")
        return 0.0
    else:
        return amount

def main():
    balance = 0.0
    is_running = True

    while is_running:
        print("**************************")
        print("     Banking Program     ")
        print("**************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter the choice(1-4):")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()  
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("**************************")
            print("That's not a valid choice")
            print("**************************")

        print("**************************")
        print("Thank you! have a nice day.")
        print("**************************")

if __name__ == '__main__':
    main()
