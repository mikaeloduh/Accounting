from calendar import monthrange
from datetime import datetime


class Accounting:

    def query_budget(self, start, end):
        data = IBudgetRepo().get_all()

        str_start = start.strftime('%Y%m')
        str_end = end.strftime('%Y%m')

        # 相差幾天
        total_number_of_date_in_the_start_month = monthrange(start.year, start.month)[1]
        total_number_of_date_in_the_end_month = monthrange(end.year, end.month)[1]

        number_of_date_in_the_start_month = total_number_of_date_in_the_start_month - start.day + 1
        number_of_date_in_the_end_month = end.day

        budget = 0
        for k, v in data.items():
            if k == str_start and (start.year == end.year) and (start.month == end.month):
                budget = budget + v.amount * (end.day - start.day + 1) // total_number_of_date_in_the_start_month
            elif k == str_start:
                budget = budget + (v.amount * number_of_date_in_the_start_month // total_number_of_date_in_the_start_month)
            elif str_start < k < str_end:
                budget = budget + v.amount
            elif k == str_end:
                budget = budget + (v.amount * number_of_date_in_the_end_month // total_number_of_date_in_the_end_month)

        return budget


class IBudgetRepo:
    db = {}

    def get_all(self):
        return self.db

    def insert_data(self, date, amount):
        str_date = date.strftime('%Y%m')
        budget = BudgetModel(date, amount)
        self.db[str_date] = budget


class BudgetModel:

    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount
