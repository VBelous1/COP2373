# Exercise 9 - Vanessa Belous

class BankAcct:
    # misc class variables for method calculations
    interest_amt = 0
    days = 0

    def __init__(self, name, acct_no, amount, interest_rate):
        self.name = name
        self.acct_no = acct_no
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest(self, new_interest):
        self.interest_rate = new_interest

    def withdraw(self, amount):
        self.amount -= amount

    def deposit(self, amount):
        self.amount += amount

    def give_balance(self):
        return self.amount

    def calc_interest(self, days):
        self.days = days
        self.interest_amt += (self.interest_rate / 100) * self.amount * days

    def __str__(self):
        return (f'\tAccount Holder: {self.name}'
                f'\n\tAccount #: {self.acct_no}'
                f'\n\tBalance: ${self.amount:,.2f}'
                f'\n\tInterest Rate: {self.interest_rate:,.2f}%'
                f'\n\tInterest Amount (after {self.days} days): ${self.interest_amt:,.2f}')

def test_class():
    # Create Unique BankAcct Object
    vbelous = BankAcct("Vanessa Belous", 12345, 500, 7)

    # Display Initial Account Details
    print("Initial Account Information:")
    print(vbelous)

    # Perform Methods
    vbelous.adjust_interest(10)
    vbelous.withdraw(50)
    vbelous.deposit(78.31)
    vbelous.give_balance()
    vbelous.calc_interest(31)

    # Display Account Details After Testing Methods
    print("\nFinal Account Information:")
    print(vbelous)

test_class()