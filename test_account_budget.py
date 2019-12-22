from main import Accounting, IBudgetRepo
import datetime
import pytest


class TestAccountingBudget:

    @pytest.fixture
    def accounting(self):
        return Accounting()

    def test_no_budget(self, accounting):
        self.create_budget_data(datetime.datetime(2020, 1, 1), 0)
        budget = accounting.query_budget(datetime.datetime(2020, 1, 1),
                                         datetime.datetime(2020, 3, 30))

        assert budget == 0

    def test_one_whole_month_budget(self):
        self.create_budget_data(datetime.datetime(2020, 1, 1), 310)
        budget = Accounting().query_budget(datetime.datetime(2020, 1, 1),
                                           datetime.datetime(2020, 1, 31))

        assert budget == 310

    def test_two_whole_month_budget(self):
        self.create_budget_data(datetime.datetime(2019, 11, 1), 300)
        self.create_budget_data(datetime.datetime(2019, 12, 31), 310)
        budget = Accounting().query_budget(datetime.datetime(2019, 11, 1),
                                           datetime.datetime(2019, 12, 31))

        assert budget == 610

    def test_one_third_month_budget(self):
        self.create_budget_data(datetime.datetime(2019, 4, 1), 300)
        budget = Accounting().query_budget(datetime.datetime(2019, 4, 1),
                                           datetime.datetime(2019, 4, 10))

        assert budget == 100

    def test_all_budget(self):
        self.create_budget_data(datetime.datetime(2078, 11, 1), 300)
        self.create_budget_data(datetime.datetime(2078, 12, 1), 200)

        budget = Accounting().query_budget(datetime.datetime(2078, 1, 1),
                                           datetime.datetime(2087, 1, 1))

        assert budget == 500

    @staticmethod
    def create_budget_data(date, amount):
        IBudgetRepo().insert_data(date, amount)
