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
from post import Post
from user import User

Form = uic.loadUiType(os.path.join(os.getcwd(),"gui_1.ui")) [0]
d1 = User()


class IntroWindow(QMainWindow,Form):
    def __init__(self):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        #Events
        self.pushButton_2.clicked.connect(self.Sign_in)
        self.pushButton_4.clicked.connect(self.watch)
        self.pushButton_8.clicked.connect(self.post_1)
        self.pushButton_6.clicked.connect(self.ediit)
        self.pushButton_5.clicked.connect(self.commentt)
        self.pushButton_3.clicked.connect(self.folllow)
        self.pushButton_9.clicked.connect(self.view_post)
        self.radioButton_2.toggled.connect(self.manage)
        #self.radioButton.toggled.connect(self.)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setEnabled(False)
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_9.setEnabled(False)

    def Sign_in(self):
        x1 = self.lineEdit.text()
        x2 = self.lineEdit_2.text()
        x3 = self.lineEdit_4.text()
        x4 = self.lineEdit_3.text()
        x5 = self.lineEdit_5.text()
        d1.login(x1,x2)
        if d1.login_status == True:
            self.textBrowser.append("you are logged in!")
            try:
                self.textBrowser.append("Here is your following request:")
                with open("follow_request_{}.txt".format(x1)) as file_object:
                    for i, line1 in enumerate(file_object):
                        self.textBrowser.append(line1)
            except FileNotFoundError:
                self.textBrowser.append("there is no following request.")
            try:
                self.textBrowser.append("Here is your acceptance_response:")
                with open("acceptance_response_for_{}.txt".format(d1.user_name)) as file_object:
                    for i, line1 in enumerate(file_object):
                        self.textBrowser.append(line1)
            except IOError:
                self.textBrowser.append("there is no acceptance_response.")
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.pushButton_6.setEnabled(True)
            self.pushButton_7.setEnabled(True)
            self.pushButton_8.setEnabled(True)
            self.pushButton_9.setEnabled(True)
        else:
            self.textBrowser.append("sorry not correct information!")

    def watch(self):
        with open("username.txt") as file_object:
            needed = file_object.readlines()
        # to track the row of data so we can show the appropriate data
        print("Here is the list of others: ")
        x1 = self.lineEdit.text()
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

    def post_1(self):
        text_post = self.lineEdit_8.text()
        a = Post(text_post)
        d1.post_list.append(a)
        self.textBrowser.append(10 * '-')
        for i in range(len(d1.post_list)):
            self.textBrowser.append("\n" + "The post content: " + "\n" + d1.post_list[i].text + "\n" + 8 * "-" + "\n" + "The date:" + str(
                    d1.post_list[i].Date) + "\n" + 8 * "-" + "\n" + "The number of your comments: " + str(
                    d1.post_list[i].num_of_comments) + "\n" + 8 * "-" + "\n" + "The list of comments: " + str(d1.post_list[i].comments))
        x1 = self.lineEdit.text()
        a.savee(x1)

    def manage(self):
        user_accepted = self.lineEdit_7.text()
        with open("acceptance_response_for_{}.txt".format(user_accepted), "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write("{}-accepted your follow request!".format(d1.user_name))

    def view_post(self):
        person_post = self.lineEdit_8.text()
        try:
            self.textBrowser.append("Here is the list of {}'s post:".format(person_post))
            with open("posts_of_{}.txt".format(person_post)) as file_object:
                for i, line1 in enumerate(file_object):
                    self.textBrowser.append(line1)
        except IOError:
            self.textBrowser.append("there is no acceptance_response.")

    def commentt(self):
        person_post = self.lineEdit_8.text()
        num_post = self.lineEdit_10.text()
        try:
            self.textBrowser.append("Enter your comment for post number {}:".format(num_post))
            comment_text = self.lineEdit_9.text()
            with open("posts_of_{}.txt".format(person_post), "a+") as file_object:
                file_object.write("\n")
                file_object.write("comment for post {}:{}".format(num_post,comment_text))
        except IOError:
            self.textBrowser.append("there is no post to comment.")

    def folllow(self):
        username = self.lineEdit_6.text()
        x = self.lineEdit.text()
        with open("follow_request_{}.txt".format(username), "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write("{} wants to follow you!".format(x))


    def ediit(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())
