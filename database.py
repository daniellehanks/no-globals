import time


class Database:
    """A simple "database".

    Similar concepts hold when using external databases.
    """
    next_id = 0

    def __init__(self):
        self._db = []

    def insert(self, row):
        print(f"Using id {self.next_id}")
        self._db.append([self.next_id, row])

        # Simulate race condition
        time.sleep(0.1)

        self.next_id += 1
        print(f"Next available id is {self.next_id}.")
