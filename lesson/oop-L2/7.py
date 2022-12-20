# Вывод объектов класса
class AgeTooSmall(Exception):
    pass

class AgeTooBig(Exception):
    pass


class User:
    MAX_AGE = 100
    MIN_AGE = 18

    def __init__(self, username, age, *args, **kwargs):
        self.username = username  # public
        self.age = age  # protected
        self._action_log = []  # protected

    @property
    def age(self):  # getter
        return self._age

    # Если все-таки надо иметь возможность изменить атрибут
    @age.setter
    def age(self, value):  # setter
        tmp_age = int(value)
        if self.MIN_AGE > tmp_age:
            raise AgeTooSmall(tmp_age)
        if not (self.MIN_AGE <= tmp_age <= self.MAX_AGE):
            raise AgeTooBig(tmp_age)
        self._age = tmp_age

    def year_older(self):
        self._age += 1

    def __str__(self): # то, как объекты видит человек
        return f'{self.__class__.__name__}: {self.username}, {self.age}'

    def __repr__(self): # то, как объекты видит шина
        return f'{self.__class__.__name__}({self.username}, {self.age})'

    # можно так вместо def __repr__(self)
    # __repr__ = __str__



class Manager(User):
    MIN_AGE = 22


class Dev(User):
    MAX_AGE = 35

    def __init__(self, username, age, level):
        super().__init__(username, age)
        self.level = level

    pass


def main():
    user_1 = Manager('i.ivanov', 22)
    user_2 = Dev('b.borisov', 32, 'junior')
    user_3 = Manager('o.olegov', 30)
    users = [user_1, user_2, user_3]

    print(users)
    for user in users:
        print(user)

try:
    main()
except AgeTooSmall as e:
    print(f'age too small: {e}')
    exit(2)
except AgeTooBig as e:
    print(f'age too big: {e}')
    exit(3)
except Exception as e:
    print(e)
    exit(1)

