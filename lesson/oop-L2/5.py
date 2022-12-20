# Кастомные исключения
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
    user_3 = Manager('o.olegov', 300)
    users = [user_1, user_2, user_3]

    for user in users:
        print(user.age)

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

