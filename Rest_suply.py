class CashBox(object):

    counter = 2

    def __new__(cls, *args, **kwargs):
        if cls.counter:
            new_obj = object.__new__(cls)
            cls.counter -= 1
            return new_obj


    def __init__(self):
        self._storage = 100

    @property
    def storage(self):
        return self._storage

    @storage.setter
    def storage(self, val):
        self._storage = val

    @storage.getter
    def storage(self):
        return f"{float(self._storage)}$"

    def putm(self, amount: int):
        self.storage += amount

    def withdrawm(self, amount):
        if amount < self.storage:
            self.storage -= amount
        else:
            print("Ran ou of cash.")