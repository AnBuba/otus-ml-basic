
# Переменные класса
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
        if not (self.MIN_AGE <= tmp_age <= self.MAX_AGE):
            raise Exception(f'wrong age: {tmp_age}')
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


user_1 = Manager('i.ivanov', 22)
user_2 = Dev('b.borisov', 32, 'junior')
user_3 = Manager('o.olegov', 30)

users = [user_1, user_2, user_3]
for user in users:
    print(user.age)
