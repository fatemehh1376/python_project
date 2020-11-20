# Python_project
import logging
import datetime
from post import Post
import hashlib
import os
from hash1 import HASH


# her we define class User to do all the things asked in project
class User():
    # to track the number of users
    track = 0

    def __init__(self):
        User.track += 1
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('creating new user!')
        self.user_name = ''
        self.pass_word = ''
        self.email = ''
        self.phone = ''
        self.bio = ''
        self.login_status = False
        self.acceptance = False
        self.following_list = []
        self.followers_list = []
        self.post_list = []

    def get_Info(self):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info("getting information from user!")
        self.user_name = input("Enter your desired username:\n ")
        with open("username.txt") as file_object1:
            for i, line in enumerate(file_object1):
                while str(line) == self.user_name + "\n":
                    self.user_name = input("please Enter another valid username,that was repeated:\n ")
        while len(self.pass_word) < 8:
            self.pass_word = input("Enter your desired password(It should be at least 8 letters):\n")
        self.bio = input("You can add bio to your profile: \n")
        self.phone = input("You can add phone number to your profile: \n")
        while len(self.phone) < 7:
            self.phone = input("please enter the correct phone number: \n")
        self.email = input("You can add email to your profile: \n")
        # here we save personal detail in txt files
        while '@' not in self.email:
            self.email = input("please add valid email to your profile:\n ")
        with open("username.txt", "a+") as file_object1:
            # Move read cursor to the start of file.
            file_object1.seek(0)
            # If file is not empty then append '\n'
            data = file_object1.read(100)
            if len(data) > 0:
                file_object1.write("\n")
            # Append text at the end of file
            file_object1.write(self.user_name)
            file_object1.write("\n")
            file_object1.write(self.bio)
            file_object1.write("\n")
            file_object1.write(self.phone)
            file_object1.write("\n")
            file_object1.write(self.email)
        with open("password.txt", "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            password = self.pass_word
            file_object.write(HASH(password))

    # here we want to check whether user name pass word are correct or not
    def login(self, username, password):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info("user is trying to login!")
        with open("username.txt") as file_object:
            for i, line1 in enumerate(file_object):
                if str(line1) == username + "\n":
                    with open("password.txt") as file_object2:
                        for j, line2 in enumerate(file_object2):
                            if j == i / 4:
                                if str(line2) == HASH(password) + "\n":
                                    self.login_status = True
        if self.login_status == True:
            print("Here is your following request:")
            with open("follow_request_{}.txt".format(username)) as file_object:
                for i, line1 in enumerate(file_object):
                    print(line1)
            self.user_name = username
            self.pass_word = password


    # here we want to see others profile
    def watch_others_profile(self):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info("user wants to see others profile!")
        with open("username.txt") as file_object:
            needed = file_object.readlines()
        # to track the row of data so we can show the appropriate data
        print("Here is the list of others: ")
        with open("username.txt") as file_object:

            for i, line1 in enumerate(file_object):
                if i % 4 == 0 and i != len(needed):
                    if str(line1) != self.user_name + "\n":
                        print(10 * "-")
                        print("username: {}".format(line1))
                        print("bio: {}".format(needed[i + 1]))
                        print("phone: {}".format(needed[i + 2]))
                        print("email: {}".format(needed[i + 3]))
                        print(10 * '-')

    # here is a function to follow a user name
    def follow(self, username):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info("user wants to follow some one!")
        with open("follow_request_{}.txt".format(username), "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write("{} wants to follow you!".format(self.user_name))
        return username

    # here is a function to accept the request
    def accept_or_not(self, username_want):
        n = int(input("Enter 1 for yes(accept),2 for no(reject)!: "))
        if n == 1:
            logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                                level=logging.INFO)
            logging.info("user accepted the follow request!")
            print("Here is the list of your followers:")
            for i in range(len(self.followers_list)):
                print(self.followers_list[i])
            self.acceptance = True
            with open("acceptance_response_for_{}.txt".format(username_want), "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write("{}-accepted your follow request!".format(self.user_name))
            return self.post_list
        if n == 2:
            self.acceptance = False
            with open("acceptance_response_for_{}.txt".format(username_want), "a+") as file_object:
                file_object.seek(0)
                data = file_object.read(100)
                if len(data) > 0:
                    file_object.write("\n")
                file_object.write("{} rejected your follow request!".format(self.user_name))


# Run part
d1 = User()
d2 = User()
d1.get_Info()
d2.get_Info()
print(15 * "-")

"---------------------------------------------"

# try to watch others profile
d1.watch_others_profile()
d2.watch_others_profile()

print(15 * "-")
name_to_follow = d1.follow("fatemeh")

# try to add post to profile and change it if needed by user
logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                    level=logging.INFO)
logging.info("user wants to do some changes in list of posts!")
a = Post("Today is a very good day!")
a.comment("your post 1!:)")
a.comment("your post 2!:)")
a.comment("your post 3!:)")
a.comment("your post 4!:)")
b = Post("Today is a very good day22!")
b.comment("your post 1!:)")
b.comment("your post 2!:)")
b.comment("your post 3!:)")
b.comment("your post 4!:)")
c = Post("How you doi'n?!")
c.comment("not good 1!:)")
c.comment("not good 2!:)")
c.comment("not good 3!:)")
c.comment("not good 4!:)")

d1.post_list.append(a)
d1.post_list.append(b)
d1.post_list.append(c)

"---------------------------------------------"
print(15 * "-")
print("Here is to show you can update your profile.")
print(15 * "-")
for i in range(len(d1.post_list)):
    d1.post_list[i].edit("Hi folks!")
    d1.post_list[i].delete()
    d1.post_list[i].comment("It's a new comment {}".format(i + 1))
    print(d1.post_list[i])
# here for liking a post
d1.post_list[2].like_pst()
"---------------------------------------------"
# try to login in this part
# try to check the acceptance result
print(15 * "-")
d4 = User()
a2 = Post("Today is a very good day!")
a2.comment("your post 1!:)")
a2.comment("your post 2!:)")
a2.comment("your post 3!:)")
a2.comment("your post 4!:)")
b2 = Post("Today is a very good day22!")
b2.comment("your post 1!:)")
b2.comment("your post 2!:)")
b2.comment("your post 3!:)")
b2.comment("your post 4!:)")
c2 = Post("How you doi'n?!")
c2.comment("not good 1!:)")
c2.comment("not good 2!:)")
c2.comment("not good 3!:)")
c2.comment("not good 4!:)")
d4.post_list.append(a2)
d4.post_list.append(b2)
d4.post_list.append(c2)
# example for a successful login
d4.login("fatemeh", "2222222222")
if d4.login_status == True:
    print("you are logged in!")
else:
    print("sorry not correct information!")

# example of an unsuccessful logging
print(15 * "-")
d3 = User()
d3.post_list.append(a)
d3.post_list.append(b)
d3.post_list.append(c)
d3.login("fatemeh", '755555555555777')
if d3.login_status == True:
    print("you are logged in!")
else:
    print("sorry not correct information!")

try:
    result = d4.accept_or_not('jack')
except ValueError:
    logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                        level=logging.WARNING)
    logging.warning("user should enter an integer!")
    print("Please Enter a digit!")
# try to check the list of posts of a user
# we should get the response first
print(15 * "-")
if result == None:
    exit()
if result != None:
    d4.followers_list.append(name_to_follow)
for i in range(len(result)):
    print(result[i])
    print("you can add your comment to this post: ")
    comm = input("Enter your comment if you wish!: ")
    if comm != "":
        result[i].comment(comm)
        print(result[i])
"---------------------------------------------"
