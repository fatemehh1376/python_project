# qt for this project
import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import logging
import datetime
import hashlib
import os
from hash1 import HASH




# we define class post to use it as an item in our profile_list
# we use logging module to save all the actions user take
# in most cases the type is INFO
class Post:
    """here we define class post with instance attributes
    text,Date,num_of_comments,comments"""

    # we define the text we want to post as an input to init
    def __init__(self, some_text):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('a post created!')
        self.text = some_text
        self.Date = datetime.datetime.now()
        self.num_of_comments = 0
        self.comments = []
        self.likes = 0

    # here we can edit the text of our post
    def edit(self, new_text):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user edits the text of the post!')
        self.text = new_text

    # here we can like a post
    def like_pst(self):
        self.likes += 1
        print("Here is the number of likes for this post: {}".format(self.likes))


    # here we want to delete a comment or post
    def delete(self):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to delete a post or a comment!')
        print("if you want to delete your post enter 1, if you want to delete a comment enter 2!")
        num = int(input("enter the number: "))
        if num == 1:
            self.text = ""
            self.Date = ""
            self.num_of_comments = 0
            self.comments = []
            print("Your post has been deleted!")
        if num == 2:
            print("which comment do you want to delete?")
            comment_num = int(input("Enter the number: "))
            try:
                self.comments.pop(comment_num - 1)
                self.num_of_comments -= 1
            except IndexError:
                logging.basicConfig(filename='app.log', filemode='w',
                                    format='%(levelname)s - %(asctime)s - %(message)s',
                                    level=logging.ERROR)
                logging.error('the number user entered for deleting a comment is out of range!')
                print("you don't have that number of comments! ")

    # we can comment for a post and append data to comment_list
    def comment(self, content):
        if self.text != "":
            self.comments.append(content)
            self.num_of_comments += 1
        else:
            pass

    # here we check whether the text is in type string or not
    # and we ask user to input a string type
    def __str__(self):
        try:
            return "\n" + "The post content: " + "\n" + self.text + "\n" + 8 * "-" + "\n" + "The date:" + str(
                self.Date) + "\n" + 8 * "-" + "\n" + "The number of your comments: " + str(
                self.num_of_comments) + "\n" + 8 * "-" + "\n" + "The list of comments: " + str(self.comments)
        except TypeError:
            logging.basicConfig(filename='app.log', filemode='w',
                                format='%(levelname)s - %(asctime)s - %(message)s',
                                level=logging.WARNING)
            logging.warning('user entered sth except string for the text of the post!')
            print("The text in your post must be in type str!")
            return ""



# here is a scenario to check the credibility of class post
# uncomment this part for trying it out
# we can comment edit or delete the post
"""
a = Post("Today is a very good day!")
a.comment("your post sucks1!:)")
a.comment("your post sucks2!:)")
a.comment("your post sucks3!:)")
a.comment("your post sucks4!:)")
a.edit("hi")
print(a)
a.delete()
print(a)
"""



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
        self.user_name = input("Enter your desired username: ")
        with open("username.txt") as file_object1:
            for i, line in enumerate(file_object1):
                while str(line) == self.user_name + "\n":
                    self.user_name = input("Enter your desired username: ")
        while len(self.pass_word) < 8:
            self.pass_word = input("Enter your desired password(It should be at least 8 letters): ")
        self.bio = input("You can add bio to your profile: ")
        while len(self.phone) < 7:
            self.phone = input("You can add phone number to your profile: ")
        self.email = input("You can add email to your profile: ")
        # here we save personal detail in txt files
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
        n = int(input("Enter one for yes(accept),two for no(reject)!: "))
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





Form = uic.loadUiType(os.path.join(os.getcwd(),"gui_1.ui")) [0]


class IntroWindow(QMainWindow,Form):
    def __init__(self):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        #Events
        self.pushButton_2.clicked.connect(self.Sign_in)
        self.pushButton_4.clicked.connect(self.watch)
        #self.pushButton_2.clicked.connect(self.say_callbk)

    def Sign_in(self):
        x1 = self.lineEdit.text()
        x2 = self.lineEdit_2.text()
        x3 = self.lineEdit_4.text()
        x4 = self.lineEdit_3.text()
        x5 = self.lineEdit_5.text()
        d1 = User()
        d1.login(x1,x2)
        if d1.login_status == True:
            self.textBrowser.append("you are logged in!")
        else:
            self.textBrowser.append("sorry not correct information!")

    def watch(self):
        with open("username.txt") as file_object:
            needed = file_object.readlines()
        # to track the row of data so we can show the appropriate data
        print("Here is the list of others: ")
        x1 = self.lineEdit.text()
        d1 = User()
        d1.user_name = x1
        with open("username.txt") as file_object:
            for i, line1 in enumerate(file_object):
                if i % 4 == 0 and i != len(needed):
                    if str(line1) != d1.user_name + "\n":
                        self.textBrowser.append(10 * "-")
                        self.textBrowser.append("username: {}".format(line1))
                        self.textBrowser.append("bio: {}".format(needed[i + 1]))
                        self.textBrowser.append("phone: {}".format(needed[i + 2]))
                        self.textBrowser.append("email: {}".format(needed[i + 3]))
                        self.textBrowser.append(10 * '-')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    w = IntroWindow()
    w.show()

    sys.exit(app.exec_())














