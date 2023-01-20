# Конвертировать цену. Статические методы
class BaseProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} ({self.__class__.__name__}): {self.price}'

    @staticmethod
    def convert_price(price, c_rate):
        return price * c_rate

class Notebook(BaseProduct):
    pass


class Phone(BaseProduct):
    pass


#def convert_price(price, c_rate):
#    return price * c_rate

