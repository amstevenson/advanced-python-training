from python_training.examples.ch2Classes.exception_handling import AttemptedOverdraw


class BankAccount:

    def __init__(self, start_balance, overdraft):
        self.balance = start_balance
        self.overdraft = overdraft
        self.od_set = False

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):

        new_balance = self.balance - withdraw_amount
        if new_balance < self.overdraft:
            raise(AttemptedOverdraw())

        self.balance -= withdraw_amount

    def get_balance(self):
        return self.balance

    def set_overdraft(self, overdraft):
        self.od_set = True
        self.overdraft = overdraft
