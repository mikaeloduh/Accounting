from Accounting import Accounting
from IBudgetRepo import IBudgetRepo
from BudgetModel import BudgetModel

import unittest
import datetime


class TestAccountingBudget(unittest.TestCase):

    def setUp(self):
        self.repo = FakeBudgetRepo()
        self.accounting = Accounting(self.repo)

    def test_no_budget(self):
        self.create_budget_data(datetime.datetime(2020, 1, 1), 0)
        budget = self.accounting.query_budget(datetime.datetime(2020, 1, 1),
                                              datetime.datetime(2020, 3, 30))

        self.assertEqual(budget, 0)

    def test_one_whole_month_budget(self):
        self.create_budget_data(datetime.datetime(2020, 1, 1), 310)
        budget = self.accounting.query_budget(datetime.datetime(2020, 1, 1),
                                              datetime.datetime(2020, 1, 31))

        self.assertEqual(budget, 310)

    def test_two_whole_month_budget(self):
        self.create_budget_data(datetime.datetime(2019, 11, 1), 300)
        self.create_budget_data(datetime.datetime(2019, 12, 31), 310)
        budget = self.accounting.query_budget(datetime.datetime(2019, 11, 1),
                                              datetime.datetime(2019, 12, 31))

        self.assertEqual(budget, 610)

    def test_one_third_month_budget(self):
        self.create_budget_data(datetime.datetime(2019, 4, 1), 300)
        budget = self.accounting.query_budget(datetime.datetime(2019, 4, 1),
                                              datetime.datetime(2019, 4, 10))

        self.assertEqual(budget, 100)

    def test_all_budget(self):
        self.create_budget_data(datetime.datetime(2078, 11, 1), 300)
        self.create_budget_data(datetime.datetime(2078, 12, 1), 200)

        budget = self.accounting.query_budget(datetime.datetime(1970, 1, 1),
                                              datetime.datetime(2087, 1, 1))

        self.assertEqual(budget, 500)

    def test_contain_no_data_multi_months(self):
        self.create_budget_data(datetime.datetime(2019, 11, 1), 300)
        self.create_budget_data(datetime.datetime(2019, 9, 1), 30)
        self.create_budget_data(datetime.datetime(2019, 12, 1), 3100)
        self.create_budget_data(datetime.datetime(2020, 1, 1), 31000)
        self.create_budget_data(datetime.datetime(2020, 12, 1), 310000)
        budget = self.accounting.query_budget(datetime.datetime(2019, 9, 1),
                                              datetime.datetime(2019, 11, 30))

        self.assertEqual(budget, 330)

    def test_cross_years(self):
        self.create_budget_data(datetime.datetime(2019, 12, 1), 3100)
        self.create_budget_data(datetime.datetime(2020, 1, 1), 31000)
        budget = self.accounting.query_budget(datetime.datetime(2019, 12, 1),
                                              datetime.datetime(2020, 1, 31))
        self.assertEqual(budget, 34100)

    def test_invalid_input(self):
        self.create_budget_data(datetime.datetime(2019, 12, 31), 3100)
        self.create_budget_data(datetime.datetime(2019, 12, 1), 31000)
        budget = self.accounting.query_budget(datetime.datetime(2019, 12, 31),
                                              datetime.datetime(2019, 11, 1))
        self.assertEqual(0, budget)

    def create_budget_data(self, date, amount):
        self.repo.insert_data(date, amount)


class FakeBudgetRepo(IBudgetRepo):

    def __init__(self):
        super(FakeBudgetRepo, self).__init__()

    def insert_data(self, date, amount):
        self.db[date.strftime('%Y%m')] = BudgetModel(date, amount)


if __name__ == '__main__':
    unittest.main()
