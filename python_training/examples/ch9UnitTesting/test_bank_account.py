import unittest
from python_training.examples.ch9UnitTesting.bank_account import BankAccount
from python_training.examples.ch2Classes.exception_handling import AttemptedOverdraw


class TestBank(unittest.TestCase):

    def test_bank_created_with_expected_values(self):
        test_bank = BankAccount(10, 15)
        self.assertEqual(test_bank.balance, 10)
        self.assertEqual(test_bank.overdraft, 15)
        self.assertFalse(test_bank.od_set)

    def test_bank_deposit(self):
        test_bank = BankAccount(10, 15)
        test_bank.deposit(20)
        self.assertEqual(test_bank.get_balance(), 30)

    def test_withdraw_success(self):
        test_bank = BankAccount(100, -100)
        test_bank.withdraw(50)
        self.assertEqual(test_bank.get_balance(), 50)

    def test_withdraw_exception_raised_exceeded_overdraft(self):
        test_bank = BankAccount(0, 0)
        with self.assertRaises(AttemptedOverdraw) as ex:
            test_bank.withdraw(500)
        self.assertEqual(str(ex.exception), 'AttemptedOverdraw exception detected')

if __name__ == '__main__':
    unittest.main()
