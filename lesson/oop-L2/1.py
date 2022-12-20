# Спрятанная переменная, getter, setter
class User:
    def __init__(self, username, age, *args, **kwargs):
        self.username = username  # public
        self.age = age  # protected
        self._action_log = [] # protected

    @property
    def age(self):  # getter
        return self._age

    # Если все-таки надо иметь возможность изменить атрибут
    @age.setter
    def age(self, value):  # setter
        age = int(value)
        if 18 <= age < 100:
            self._age = age
        else:
            print('wrong')

    def year_older(self):
        self._age += 1


class Manager(User):
    pass


class Dev(User):
    def __init__(self, username, age, level):
        super().__init__(username, age)
        self.level = level
    pass


user_1 = Manager('i.ivanov', 22)
user_2 = Dev('b.borisov', 32, 'junior')
user_3 = Manager('o.olegov', 400)

user_3.age = '150'

users = [user_1, user_2, user_3]
for user in users:
    print(user.age)
