import logging
import datetime
import csv
import time
from asyncio import sleep
from hashlib import sha256


class Profile:
    id = ()
    data = []
    img = []

    def __init__(self, user, password, flag, email, phone_no, status, comment, follower, following):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('a profile is created!')

        self.user = user
        self.password = password

        self.flag = flag
        self.email = email
        self.phone_no = phone_no
        self.status = status
        self.comment = comment
        self.follower = follower
        self.following = following

    def save_user_and_pass(self, user, password):

        global data
        data = []
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user defines his/her user and password and save them!')

        if len(self.user) >= 5 and len(self.password) >= 6:
            a = sha256(self.user.encode()).hexdigest()
            b = sha256(self.password.encode()).hexdigest()

            data.append(self.user)
            data.append(b)

        return self.user

    def bio(self, status):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to enter his/her bio!')


        data.append(self.status)

        return self.bio

    def enter_email(self, email):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to enter the email!')

        if '@' in self.email or self.email == "":
            data.append(self.email)

        return self.email

    def phone_nu(self, phone_no):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user  enters the phone_no!')

        data.append(phone_no)
        with open('data.csv', 'a+', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(data)

        return phone_no

    def infos_users(self, user):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user added to the file and saved!')
        with open('users.csv', 'a+', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow("@" + str(self.user))
        return "@" + self.user


class Login:

    def __init__(self, enteruser, enterpass):
        self.enteruser = enteruser
        self.enterpass = enterpass
        self.login_status = ""

    def login1(self, enteruser, enterpass):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to login to his/her profile!')

        bb = sha256(self.enterpass.encode()).hexdigest()

        with open('data.csv', newline='') as csvfile:

            # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            lines = csvfile.readlines()

            for m in range(0, len(lines)):
                row = lines[m].split()
                if row[0] == self.enteruser:
                    if row[1] == bb:

                        self.login_status = True
                        print("you will able to login")
                        print("hi")
                    else:
                        self.login_status = False
                        print(("you can't log in!!"))

        return self.login_status


class Searching_people():

    def __init__(self, user_find,userr):
        self.user_find = user_find
        self.userr=userr
    def searching(self, user_find):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to search for another profile!')

        with open('users.csv', newline='') as csvfile:

            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

            for row in spamreader:

                if list(self.user_find) == row:
                    with open('data.csv', newline='') as csvfile:

                        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

                        for line in spamreader:

                            ee = self.user_find.split('@')

                            if line[0] == ee[1]:
                                print("the  information of  profile  that you searched: \n")
                                for i in range(0, len(line)):
                                    if i != 1:
                                        print("   ****************\n" + line[i] + "   ***************\n")
                                        pass

    def following(self,user_find,userr):

        no_following = 0
        f1 = []
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to follow another users!')


        f1.append(self.userr)

        if self.user_find!=self.userr:


                    if self.user_find not in f1:

                                        no_following += 1

                                        f1.append(self.user_find)
                                        with open('following.csv', 'a+', newline='') as csvfile:

                                            spamwriter = csv.writer(csvfile, delimiter=' ',
                                                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
                                            spamwriter.writerow(str(f1))


        return f1 , no_following


    def follower(self, follower_list):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user followed by another users!')

        no_follower = 0
        f2 = []
        f2.append(self.user_find)
        no_follower += 1
        return f2, no_follower




# we define class post to use it as an item in our profile_list
# we use logging module to save all the actions user take
# in most cases the type is INFO
class Post:
    """here we define class post with instance attributes
    text,Date,num_of_comments,comments"""

    # we define the text we want to post as an input to init
    time.sleep(4)
    def __init__(self, some_text):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('a post created!')
        self.text = some_text
        self.Date = datetime.datetime.now()
        self.num_of_comments = 0
        self.comments = []
        self.likes = []

    # here we can edit the text of our post
    def edit(self, new_text):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user edits the text of the post!')
        self.text = new_text

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



    def like_pst(self, like):
        self.likes.append(like)
        count_of_likes = self.likes + 1

    # we can comment for a post and append data to comment_list
    def comment(self, content):
        self.comments.append(content)
        self.num_of_comments += 1

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




def main():
    vu = []
    q = int(input("please enter the number:\n1-you want to login!!!\n 2-you want to make a profil!!\n"))
    if q == 2:
        with open('data.csv', 'r', newline='') as csvfile:

            lines = csvfile.readlines()

            u = input("enter your personal user(more than 5 chars):\n")

            for m in range(0, len(lines)):
                lu = lines[m].split()
                # print(lu[0])
                vu.append(lu[0])

            while u in vu:
                u = input("please enter another user(more than 5 chars):\n")
            else:
                pass

            p = input("enter your security password(more than 6 chars):\n")
            k = input("if you like writ about yourself:\n")
            e = input("enter your valid email:\n")

            ph = input(" type your  phone_no: \n ")

            b = Profile(u, p, 0, e, ph, k, 0, 0, 0)
            b.save_user_and_pass(u, p)
            b.bio(k)
            b.enter_email(e)
            b.phone_nu(ph)
            b.infos_users(u)
            print("your  profile compeleted:\n" + "    *******************      ", "user=", u, "\n email=", e,"\n bio=",k,
                  "\n phone_number=", ph , "   *******************     \n")
            eu = input("enter your user for getting login:\n")
            ep = input("enter your password  for getting login:\n")

            c = Login(eu, ep)
            c.login1(eu, ep)
            if c.login_status == True:
                a = Post("Today is a very good day!")
                a.comment("your post sucks1!:)")
                a.comment("your post sucks2!:)")
                a.comment("your post sucks3!:)")
                a.comment("your post sucks4!:)")
                a.edit("hi")
                print(a)
                a.delete()
                print(a)
                a.edit(1)
                g = input("do you want to find your friends? if you  want type her id:")
                h = Searching_people(g,u)
                print(h.searching(g))
                j = int(input("do you want to follow this profile? 1-yes 2-no\n"))
                if j == 1:
                    print("profiles that you followed and the number of following people : \n")
                    print(h.following(g,u))
                else:
                    pass

    if q == 1:
        eu = input("enter your user for getting login:\n")
        ep = input("enter your password  for getting login:\n")
        with open('data.csv', 'r', newline='') as csvfile:

            lines = csvfile.readlines()



            for m in range(0, len(lines)):
                lu = lines[m].split()


            c = Login(eu, ep)
            c.login1(eu, ep)
            if c.login_status == True:

                a = Post("Today is a very good day!")
                a.comment("your post sucks1!:)")
                a.comment("your post sucks2!:)")
                a.comment("your post sucks3!:)")
                a.comment("your post sucks4!:)")
                a.edit("hi")
                print(a)
                a.delete()
                print(a)
                a.edit(1)
                g = input("do you want to find your friends? if you  want type her id:")
                h = Searching_people(g,eu)
                print(h.searching(g))
                j = int(input("do you want to follow this profile? 1-yes 2-no\n"))

                if j == 1:
                    print("profiles that you followed and the number of following people : \n")
                    print(h.following(g,eu))
                else:
                    pass


main()