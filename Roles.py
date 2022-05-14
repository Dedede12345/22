class Employee(object):

    def __init__(self, name: str, age: int, longevity):
        self.name = name
        self.age = age
        self.longevity = longevity


class Cook(Employee):

    def __init__(self, name: str, age: int, longevity):
        super(Cook, self).__init__(name, age, longevity)

    def cooksmth(dish: str):  # C protected
        print(f"In process of cooking {dish}...")
        return dish


class Waiter(Employee):

    def __init__(self, name: str, age: int, longevity):
        super(Waiter, self).__init__(name, age, longevity)

    def serve(self, dish):
        print(f"Your {dish} has been served.")

    def bill(self):
        print("Bring bill.")  # otherwise dish class is needed
        return None


class Client:

    def __init__(self, name):
        self.name = name