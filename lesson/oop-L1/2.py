# inheritance
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = int(age)

    def year_older(self):
        self.age += 1


class Manager(User):
    pass


class Dev(User):
    pass


user_1 = Manager('i.ivanov', '22')
user_2 = Dev('b.borisov', 32)
user_3 = Manager('o.olegov', 28)

users = [user_1, user_2, user_3]
for user in users:
    print(user.username, user.age)
    user.year_older()
