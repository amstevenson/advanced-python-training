from advanced_python_training.examples.ch2Classes.exception_handling import AttemptedOverdraw

from threading import Thread, Event
import queue

# Task outline

# initially, 0 in the bank, 1 thread polling 10 pounds a second

# 1 other thread 50 quid, polling, can I have, can I have

# after 5 seconds, will have 50 pounds, so it can then access it


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


def withdrawer():
    while True:
        item = q.get()
        if item is None:
            break
        print('withdrawing {} pounds'.format(item))
        bank.withdraw(item)
        q.task_done()


class Depositer(Thread):
    def __init__(self, amount, account):
        super().__init__()
        self.amount = amount
        self.account = account

    def run(self):
        for i in range(0, 10):
            bank.deposit(10)
            amount = bank.get_balance()
            print(amount)

            if amount > 50:
                print('enough funds in bank')
                q.put(50)

if __name__ == '__main__':
    # Create account
    bank = BankAccount(0, 0)
    print("Initial balance: {}".format(bank.get_balance()))

    event = Event()

    # create a queue
    q = queue.Queue()
    threads = []
    for i in range(2):  # Only one thread for now
        t = Thread(target=withdrawer)
        t.start()
        threads.append(t)

    q.join()

    # Create depositor / withdrawer
    deposit = Depositer(10, bank)
    deposit.start()

    for i in range(1):
        q.put(None)
    for t in threads:
        t.join()

    deposit.join()
