# __iter__ / __len__ / __contains__
import re

class BaseProduct:
    NAME_RE = re.compile(r'[a-zA-Z0-9 ]+')

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} ({self.__class__.__name__}): {self.price}'

    @classmethod
    def _name_validator(cls, name):
        if not cls.NAME_RE.fullmatch(name):
            raise ValueError(name)
        return name

    @staticmethod
    def convert_price(price, c_rate):
        return price * c_rate

    @classmethod
    def create_conv_price(cls, name, price, c_rate=1.1):
        cls._name_validator(name)
        inst = cls(name, cls.convert_price(price, c_rate))
        return inst


class Notebook(BaseProduct):
    pass


class Phone(BaseProduct):
    @staticmethod
    def convert_price(price, c_rate):
        return price * c_rate * 0.95


class Basket:
    def __init__(self):
        self._products = {}

    def add(self, product):
        if not product in self._products:
            self._products[product] = 1
        else:
            self._products[product] += 1

    def __str__(self):
        return f'{self._products}'

    def __iter__(self):
        return ((el.name, qty) for el, qty in self._products.items())

    def __len__(self):
        return sum(el[1] for el in self)

    def __contains__(self, item):
        return item in self._products


prod_1 = Notebook('ZenBook 4', 589.5)
prod_2 = Phone.create_conv_price('Galaxy S22', 975.4, 0.650)

basket_1 = Basket()
basket_1.add(prod_1)
basket_1.add(prod_2)
basket_1.add(prod_2)

print(basket_1)

for el in basket_1:
    print(el)

print(len(basket_1))

print(prod_1 in basket_1)



