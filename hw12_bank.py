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
        if not self.client_is_registered:
            self.deposit_is_open = False
            return "Only a registered client can open a deposit."

        self.deposit_is_open = True
        self.start_balance = start_balance
        self.years = years
        self.client_id = client_id
        return f'{self.name}, you have opened a deposit.'

    def calc_deposit_interest_rate(self, client_id):

        if not self.deposit_is_open:
            return None

        self.client_id = client_id
        percent_years = 0.10
        month = self.years * 12
        percent_month = percent_years / 12
        return round(self.start_balance * (1 + percent_month) ** month, 2)

    def close_deposit(self, client_id):
        if self.deposit_is_open is True:
            total = self.calc_deposit_interest_rate(client_id)
            return total
        return None


CLIENT_ID = "0000001"

bank = Bank()


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


class CurrencyConverter:

    def __init__(self):
        self.exchange_rates = {'BYN': 1.0, 'USD': 2.9364, 'EUR': 3.3894, 'RUB': 3.7179}

    def exchange_currency(self, currency, amount, to_currency='BYN'):

        if currency not in self.exchange_rates:
            return print("Unknown currency")
        if to_currency not in self.exchange_rates:
            return print("Unknown currency")

        total_byn = amount * self.exchange_rates[currency]
        total_other = total_byn / self.exchange_rates[to_currency]
        return round(total_other, 2), to_currency


converter = CurrencyConverter()

vasya = Person('USD', 10)
petya = Person('EUR', 5)

# Если валюта не задана, то конвертация происходит в BYN:
assert converter.exchange_currency(vasya.currency, vasya.amount) == (29.36, "BYN"), \
    'Incorrect conversion value'
assert converter.exchange_currency(petya.currency, petya.amount) == (16.95, "BYN"), \
    'Incorrect conversion value'

# Конвертация из BYN в заданную валюту:
assert converter.exchange_currency(vasya.currency, vasya.amount, 'EUR') == (8.66, "EUR"), \
    'Incorrect conversion value'
assert converter.exchange_currency(petya.currency, petya.amount, 'USD') == (5.77, "USD"), \
    'Incorrect conversion value'
assert converter.exchange_currency(petya.currency, petya.amount, 'RUB') == (4.56, "RUB"), \
    'Incorrect conversion value'
