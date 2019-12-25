from calendar import monthrange
from datetime import datetime


class Accounting:

    def __init__(self, budget_repo):
        self.repo = budget_repo

    def query_budget(self, start, end):
        str_start = start.strftime('%Y%m')
        str_end = end.strftime('%Y%m')

        # 相差幾天
        total_date_start_month = monthrange(start.year, start.month)[1]
        total_date_end_month = monthrange(end.year, end.month)[1]

        date_start_month = total_date_start_month - start.day + 1
        total_budget = 0
        for k, v in self.repo.get_all().items():
            if k == str_start and (start.year == end.year) and (start.month == end.month):
                total_budget = v.amount * (end.day - start.day + 1) // total_date_start_month
                break
            elif k == str_start:
                total_budget = v.amount * date_start_month // total_date_start_month
            elif str_start < k < str_end:
                total_budget = total_budget + v.amount
            elif k == str_end:
                total_budget = total_budget + (v.amount * end.day // total_date_end_month)
                break

        return total_budget
