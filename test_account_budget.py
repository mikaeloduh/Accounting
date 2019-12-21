from main import Accounting, IBudgetRepo
import datetime


class TestAccountingBudget():
    def test_no_budget(self):
        self.create_budget_data(datetime.datetime(2020, 1, 1), 0)
        budget = Accounting().query_budget(datetime.datetime(2020, 1, 1),
                                           datetime.datetime(2020, 3, 30))

        assert budget == 0

    def test_one_month_budget(self):
        self.create_budget_data(datetime.datetime(2020, 1, 1), 310)
        budget = Accounting().query_budget(datetime.datetime(2020, 1, 1),
                                           datetime.datetime(2020, 1, 31))

        assert budget == 310

    def test_two_month_budget(self):
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

    # def test_get_all_budget(self):
    #     self.create_budget_data('201911', 300)
    #     self.create_budget_data('201912', 310)
    # def test_one_mouth():
    #     pass

    @staticmethod
    def create_budget_data(date, amount):
        IBudgetRepo().insert_data(date, amount)