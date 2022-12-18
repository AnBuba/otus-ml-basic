# mixin
class CanPhoneCallMixin:
    def client_call(self, phone_num, msg):
        # phone_num
        print(f'Hello {self.username}! {msg}')


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = int(age)

    def year_older(self):
        self.age += 1


class Manager(CanPhoneCallMixin, User):
    pass


class Staff(CanPhoneCallMixin, User):
    pass


class Dev(User):
    pass


user_1 = Manager('i.ivanov', '22')
user_2 = Dev('b.borisov', 32)
user_3 = Staff('o.olegov', 28)

user_3.client_call('9999999', 'good morning!')

users = [user_1, user_2, user_3]
for user in users:
    print(user.username, user.age)
    user.year_older()
    if isinstance(user, CanPhoneCallMixin):
        user.client_call('9999999', 'hello!')