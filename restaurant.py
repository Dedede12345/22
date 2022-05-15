from Roles import Cook, Waiter, Client
from Rest_suply import CashBox


class Restaurant:

    def __init__(self, cook: Cook, waiter: Waiter):  # *employees
        self.cash_box = CashBox()
        self.cook = cook
        self.waiter = waiter
        # self.employees = employees

    def greet_client(self, client: Client):
        print(f"Greetings, {client.name}")


class Delivery(Restaurant):

    def __init__(self, deliverer: Waiter, cook: Cook):
        super(Delivery, self).__init__(cook, deliverer)
        self.owns_a_truck = True

    @staticmethod
    def knock_door(self):
        print("Knock, Knock...")  # Here is Johny.


# Employees
cook1 = Cook("Gordon Ramsay", 55, 56)
waiter1 = Waiter("Mathew", 20, 1)

# Restaurant
client = Client("Gelb")

restaurant = Restaurant(cook1, waiter1)
print(restaurant.cash_box.storage)

# Delivery
deliverer = Waiter("Sam", 24, 4)
delivery = Delivery(deliverer, cook1)

print(delivery.cash_box.storage)
