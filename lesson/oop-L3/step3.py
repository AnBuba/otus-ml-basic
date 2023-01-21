# улучшение step2
class BaseProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} ({self.__class__.__name__}): {self.price}'

    @staticmethod
    def convert_price(price, c_rate):
        return price * c_rate

    @staticmethod
    def create_conv_price(name, price, c_rate=1.1):
        inst = BaseProduct(name, convert_price(price, c_rate))
        return inst

class Notebook(BaseProduct):
    pass


class Phone(BaseProduct):
    pass


def convert_price(price, c_rate):
    return price * c_rate

prod_1 = Notebook('ZenBook 4', 589.5)
prod_2 = Phone('Galaxy S22', Phone.convert_price(975.4, 0.650))
prod_3 = BaseProduct.create_conv_price('base', 100, 0.65)
print(prod_1)
print(prod_2)
print(prod_3)
