# сначала идут импорты из стандартных библиотек,
import random

# затем импорт библиотек установленных pip,
# import cv2

# затем локальные
import db

RATES = {
    'USD': random.randint(35, 120),
    'EUR': random.randint(40, 140),
}


def get_currency_rate(currency):
    return RATES.get(currency)

# чтобы можно было потестировать, и не запусалась  из __main__
if __name__ == '__main__':
    rate_1 = get_currency_rate('USD')
    rate_2 = get_currency_rate('EUR')
    db.write_to_db('USD', rate_1, '27/12/2022 23:10:15')
    print(rate_1, rate_2)