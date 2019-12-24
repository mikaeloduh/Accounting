class IBudgetRepo:

    def __init__(self):
        self.db = {}

    def get_all(self):
        return self.db
