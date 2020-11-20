# Python_project
import logging
import datetime


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