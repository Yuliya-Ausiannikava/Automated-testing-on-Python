"""
A class with methods for calculating profit from a bank deposit
with monthly capitalization has been created.
"""


class Bank:

    def __init__(self):
        self.name = None
        self.client_id = None
        self.start_balance = 0
        self.years = 0
        self.client_is_registered = None
        self.deposit_is_open = None

    def register_client(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.client_is_registered = True
        return print(f'{self.name}, registration was successful.')

    def open_deposit_account(self, client_id, start_balance, years):
        self.start_balance = start_balance
        self.years = years
        self.client_id = client_id
        if self.client_is_registered is True:
            self.deposit_is_open = True
            return print(f'{self.name}, you have opened a deposit.')
        else:
            self.deposit_is_open = False
            return print("Only a registered client can open a deposit.")

    def calc_deposit_interest_rate(self, client_id):
        self.client_id = client_id
        percent_years = 0.10
        month = self.years * 12
        percent_month = percent_years / 12
        final_amount = self.start_balance * (1 + percent_month) ** month
        if self.deposit_is_open is True:
            return round(final_amount, 2)
        else:
            return None

    def close_deposit(self, client_id):
        if self.deposit_is_open is True:
            total = self.calc_deposit_interest_rate(client_id)
            return total
        else:
            return None


CLIENT_ID = "0000001"

bank = Bank()
bank.register_client(client_id=CLIENT_ID, name="Siarhei")
bank.open_deposit_account(client_id=CLIENT_ID, start_balance=1000, years=1)

assert bank.calc_deposit_interest_rate(client_id=CLIENT_ID) == 1104.71, \
    "Income from the deposit was calculated incorrectly"
bank.close_deposit(client_id=CLIENT_ID)
