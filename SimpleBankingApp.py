
accounts = { 'ayo' : { 'password' : '3822', 'balance' : 1200.0 } }


def createAccount() :
    # Take a unique name for account creation
    accountName = input("\nEnter a unique name here: ").lower()
    # Check if account already exists in the database.
    if accountName in accounts.keys() :
        print("Sorry! Account already exists")
        # Go back to the landing page
        main()
    else :    
        # Take password for the new account.
        password = input("Enter your desired password here: ")
        # Set balance to 0.0
        balance = float()
        # Insert new account into the data store
        accounts[accountName] = { 'password' : password, 'balance' : balance }
    print("\nAccount created successfully!")
    # Go back to the landing page
    main()

def tranction() :
    # Take an account name for account login
    accountName = input("\nEnter account name here: ").lower()
    # Check if account name exists in the data store.
    if accountName in accounts.keys() :
        # Take password for the new account.
        password = input("Enter password here: ")
        # Authenticate login
        if password == accounts[accountName]['password'] :
            print("\nSelect an option below.\nPress 1 to check balance\nPress 2 to deposit.\
                \nPress 3 to withdraw cash.\nPress 4 to transfer funds.\n")
            # Take choice of transaction selection
            choice = int(input("Enter your preferred selection here: "))
            if choice == 1:
                checkBalance(accountName)
            elif choice == 2 :
                depositCash(accountName)
            elif choice == 3 :
                withdrawCash(accountName)
            elif choice == 4 :
                transferCash(accountName)
            else :
                print("Not a valid key. Try again!")
                # Go back to the landing page
                main()
        else :
            print("Sorry! Password is incorrect")
        # Go back to the landing page
        main()

def checkBalance(accountName) :
    print("Your balance is: ", accounts[accountName]['balance'])
    # Go back to the landing page
    main()

def depositCash(accountName) :
    balance = accounts[accountName]['balance']
    amount = float( input("\nEnter the amount you want to deposit here: ") )
    balance += amount
    # Update balance
    accounts[accountName]['balance'] = balance
    print("Your new balance is: ", accounts[accountName]['balance'])
    # Go back to the landing page
    main()

def withdrawCash(accountName) :
    balance = accounts[accountName]['balance']
    amount = float( input("\nEnter the amount you want to withdraw here: ") )
    balance -= amount
    # Update balance
    accounts[accountName]['balance'] = balance
    print("Your new balance is: ", accounts[accountName]['balance'])
    # Go back to the landing page
    main()

def transferCash(accountName) :
    balance = accounts[accountName]['balance']
    beneficiary = input("\nEnter beneficiary account name here: ").lower()
    # Check if beneficiary exists in the data store
    if beneficiary in accounts.keys() :
        # Take beneficiary's balance
        b_balance = accounts[beneficiary]['balance']
        # Take the amount to be transferred
        amount = float( input("Enter the amount you want to transfer here: ") )
        # Check if benefactor has enough in his balance
        if balance < amount :
            print("Sorry! Not enough balance for this transaction.")
            # Go back to the landing page
            main()
        else :
            b_balance += amount
            balance -= amount
            # Update balance
            accounts[beneficiary]['balance'] = b_balance
            accounts[accountName]['balance'] = balance
        print("Your new balance is: ", accounts[accountName]['balance'])
        # Go back to the landing page
        main()
    else :
        print("Error! Beneficiary not found.\nTry again.")
        # Go back to the landing page
        main()


def main():
    print("##########################################################################################################")
    print("\nYou are welcome to My Banking App landing page. Make a selection below for your desire choice of service.\
            \nPress 1 to create an account.\nPress 2 to conduct a transaction.\nPress 0 to close app.\n")
    print("Available accounts with their balance")
    for acc in accounts.keys() :
        print(acc, accounts[acc]['balance'])
    # Take desire selection
    choice_selection = int(input("Enter your preferred selection here: "))
    # Choose action based on choice selection
    if choice_selection == 1 : createAccount()
    elif choice_selection == 2 : tranction()
    elif choice_selection == 0 : 
        print("\nThanks for using this app. Goodbye!")
        pass
    else : print("Not a valid key. Try again!")

if __name__ == '__main__' :
    main()