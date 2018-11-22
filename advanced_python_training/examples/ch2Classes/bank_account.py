from advanced_python_training.examples.ch2Classes.exception_handling import AttemptedOverdraw
from advanced_python_training.examples.ch2Classes.person import Person
from advanced_python_training.examples.ch2Classes.employee import Employee


class BankAccount:

    def __init__(self, start_balance, overdraft):
        self.balance = start_balance
        self.overdraft = overdraft

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):

        new_balance = self.balance - withdraw_amount
        if new_balance - self.overdraft:
            raise(AttemptedOverdraw())

        self.balance -= withdraw_amount

    def get_balance(self):
        return self.balance

    def set_overdraft(self, overdraft):
        self.overdraft = overdraft

if __name__ == '__main__':
    # Test 1, deposit ok
    bank = BankAccount(0, 0)
    bank.deposit(200)
    print(bank.get_balance())

    # Test 2, bank withdraw exception
    try:
        exception_test = BankAccount(0, 0)
        bank.withdraw(10)
    except AttemptedOverdraw as ex:
        print(ex)

    # Test 3, person
    person = Person('joe', 'bob', 20)
    print(person.get_person())

    # Test 4, employee get person
    employee = Employee('joe', 'doe', 20, 'derp head', '20000')
    print(employee.get_person())

