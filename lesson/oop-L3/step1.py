class BaseProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} ({self.__class__.__name__}): {self.price}'


class Notebook(BaseProduct):
    pass


class Phone(BaseProduct):
    pass


prod_1 = Notebook('ZenBook 4', 589.5)
prod_2 = Phone('Galaxy S22', 472.4)
print(prod_1)
print(prod_2)
