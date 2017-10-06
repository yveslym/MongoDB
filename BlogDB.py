from pymongo import MongoClient
from mongoengine import *

client = MongoClient('localhost', 27017)
db = client['BlogDB']
connect('BlogDB')
users = db.users
posts = db.posts


class User(Document):
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    email = StringField(required=True)
    comments = ListField(EmbeddedDocumentField(Comment))

    def save_user(self):
        users = db.users
        self.save()



class Post(Document):
    title = StringField(max_length=100, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    meta = {'allow_inheritance': True}
    tags = ListField(StringField(max_length=30))

    def save_user(self):
        post = db.posts




class Text_Post(Post):
    content = StringField()


class Image_Post(Post):
    image_path = StringField()


class Link_Post(Post):
    link_url = StringField()


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=20)



if __name__ == '__main__':

    Yves = User(
        first_name = 'Yves',
        last_name = 'Songolo',
        email = 'yves2300@yahoo.fr'
    ).save()

    Charmele = User(
        first_name='Charmelle',
        last_name='Simtofu',
        email='charmelle@gmail.com'
    ).save()




    print("ok")
