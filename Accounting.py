

class Accounting:

    def __init__(self, budget_repo):
        self.repo = budget_repo

    def query_budget(self, start, end):
        str_start = start.strftime('%Y%m')
        str_end = end.strftime('%Y%m')

        total_budget = 0
        for k, v in self.repo.get_all().items():
            if k == str_start and (start.year == end.year) and (start.month == end.month):
                total_budget = v.amount * (end.day - start.day + 1) // v.days_in_month()
                break
            elif k == str_start:
                total_budget = total_budget + v.amount * (v.days_in_month() - start.day + 1) // v.days_in_month()
            elif str_start < k < str_end:
                total_budget = total_budget + v.amount
            elif k == str_end:
                total_budget = total_budget + (v.amount * end.day // v.days_in_month())

        return total_budget
