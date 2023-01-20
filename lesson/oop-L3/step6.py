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


prod_1 = Notebook('ZenBook 4', 589.5)
prod_2 = Phone.create_conv_price('Galaxy S22', 975.4, 0.650)
prod_3 = BaseProduct.create_conv_price('base', 100, 0.65)
print(prod_1)
print(prod_2)
print(prod_3)
