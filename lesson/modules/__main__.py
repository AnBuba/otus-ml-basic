import sys
import os
import random

from utils import get_currency_rate

# чтобы все работа из терминала (нахождение модулей для импорта)
ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '../'
))
print(ROOT)
sys.path.append(ROOT)

def main():
    currency = ('USD', 'EUR')[random.randint(0, 1)]
    rate = get_currency_rate(currency)
    print(f'{currency}: {rate}')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        exit(1)

