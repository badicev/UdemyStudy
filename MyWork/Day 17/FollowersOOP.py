'''
class User:
    pass


user_1 = User()
user_1.id = "001"
user_1.username = "basak"

print(user_1.username)

user_2 = User()
user_2.id = "001"
user_2.username = "basak"

print(user_2.username)

#instead --> initialize

'''

class User:

    def __init__(self, id, username):
        print("New user being created...")
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following +=1

user_1 = User("001", "badiçe")
user_2 = User("002", "angela")

print(user_1.id)


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.followers)
