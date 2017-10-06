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


    def save_user(self):
        users = db.users
        self.save()


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=20)

class Post(Document):
    title = StringField(max_length=100, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    meta = {'allow_inheritance': True}
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    def save_post(self):
        post = db.posts
        self.save()




class Text_Post(Post):
    content = StringField()


class Image_Post(Post):
    image_path = StringField()


class Link_Post(Post):
    link_url = StringField()






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
    )
    Charmele.save_user()
    Yves.save_user()

    post1 = Text_Post(
        title = 'first step in mongo db',
        content = 'Took a look at MongoEngine today, looks pretty cool.',
        tags = ['mongodb','mongoengine'],
        author = Yves
    )
    #post1.comments =[' wow']
    post1.save_post()

    post2 = Link_Post(title='MongoEngine Documentation', author=Charmele)
    post2.link_url = 'https://github.com/yveslym/MongoDB'
    post2.tags = ['mongoengine']
    #post2.comments = [' like this', 'yes, was super great']
    post2.save_post()

    for post in Post.objects:
        print(post.title)
        print('=' * len(post.title))

        if isinstance(post, Text_Post):
            print(post.content)

        if isinstance(post, Link_Post):
            print('Link: {}'.format(post.link_url))




    print("ok")
