class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw money
    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds.")
        elif amount > 0:
            self.amount -= amount
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Withdrawal amount must be positive.")

    # Change interest rate
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate
        print(f"Interest rate changed to {new_rate:.2f}%")

    # Return balance
    def get_balance(self):
        return self.amount

    # Calculate interest based on number of days
    def calculate_interest(self, days):
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    # String representation
    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2f}%")

# Test Function
def test_bankacct():
    # Create account
    acct = BankAcct("Carl Jackson", "123456", 1000.00, 4.5)

    print("Initial Account Information")
    print(acct)
    print()

    # Deposit
    acct.deposit(500)
    print(f"Current Balance: ${acct.get_balance():.2f}\n")

    # Withdraw
    acct.withdraw(200)
    print(f"Current Balance: ${acct.get_balance():.2f}\n")

    # Adjust interest rate
    acct.adjust_interest_rate(5.0)
    print()

    # Calculate interest for 30 days
    interest = acct.calculate_interest(30)
    print(f"Interest earned in 30 days: ${interest:.2f}\n")

    # Display final account information
    print("Final Account Information")
    print(acct)

# Run test function
test_bankacct()