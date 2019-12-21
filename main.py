import datetime
from calendar import monthrange


class Accounting:
    def query_budget(self, start, end):
        # '202001' '202002' '202003'
        data = IBudgetRepo().get_all()

        str_start = start.strftime('%Y%m')
        str_end = end.strftime('%Y%m')

        # 相差幾天
        number_of_date_start = end.day - start.day + 1
        number_of_date_end = end.day - start.day + 1
        print(number_of_date)
        #
        number_of_date_in_the_start_month = monthrange(start.year, start.month)[1]
        number_of_date_in_the_end_month = monthrange(end.year, end.month)[1]

        budget = 0
        for k, v in data.items():
            if k == str_start:
                budget += v.amount *
            if k == str_end:

            # n[str_start].year_month
            # n[str_end].year_month
        return budget * number_of_date // (number_of_date_in_the_start_month +
                                           number_of_date_in_the_end_month)
        # budget = data.get(start)
        # return budget


class IBudgetRepo:
    db = {}

    def get_all(self):
        return self.db

    def insert_data(self, date, amount):
        str_date = date.strftime('%Y%m')
        budget = BudgetModel(date, amount)
        self.db[str_date] = budget


class BudgetModel():
    year_month = ''
    amount = 0

    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount


# if __name__ == "__main__":
#     budget = Accounting().query_budget(1, 2)
#     print(budget)