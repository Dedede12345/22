class RandomCls(object):

    @staticmethod
    def say_hello():
        print("Hello, world")

    @classmethod
    def hello(cls):
        print(f"Hello, it's {cls.__name__}.")

    def __new__(cls, *args, **kwargs):
        print("new")
        return super(RandomCls, cls).__new__(cls)


RandomCls.say_hello()
RandomCls.hello()

a = RandomCls(object)
b = object.__new__(RandomCls)

b.say_hello()

c = RandomCls.__new__(RandomCls)
