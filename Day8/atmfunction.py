balance = 2000

# Function to display the main menu
def display_menu():
    print("==== ATM MENU ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# Function to check account balance
def check_balance():
    print("Your current balance is $" + str(balance))

# Function to deposit money into the account
def deposit_money():
    global balance
    amount = float(input("Enter the amount you want to deposit: "))
    balance += amount
    print("$" + str(amount) + " has been deposited into your account.")
    print("Your new balance is $" + str(balance))

# Function to withdraw money from the account
def withdraw_money():
    global balance
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("$" + str(amount) + " has been withdrawn from your account.")
        print("Your new balance is $" + str(balance))
    else:
        print("Insufficient funds. Your balance is $" + str(balance))

# Main function to run the ATM program
def main():
    print("Welcome to the ATM!")
    while True:
        display_menu()
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()