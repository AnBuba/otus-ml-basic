class User:
    def __init__(self, username, age, phone=None):
        self.username = username
        self.age = int(age)
        self.phone = phone

    def year_older(self):
        self.age += 1

# print(type(User), User)

# user_1 = User() # __call__ | instance
# print(user_1, vars(user_1))
# print(user_1.username)

user_1 = User('i.ivanov', '22') # immutable: str, tuple, in, float | mutable: list, set, dict
user_2 = User('b.borisov', 32)
user_3 = User('o.olegov', 28)
# print(vars(user_1))
# print(user_1.username, user_1.age)

users = [user_1, user_2, user_3]
for user in users:
    print(user.username, user.age, user.phone)
    user.year_older()