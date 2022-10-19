import base64
from datetime import datetime, timedelta
from types import NoneType
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)
app.config["SECRET_KEY"] = 'jp0?ad[1-=-0-`94mpgf-pjmwr3;2owdakdnw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''
from db import db
db.create_all()
exit()
'''


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(500), nullable=True)
    logo = db.Column(db.LargeBinary)
    photo = db.relationship('Posts', backref='users')
    favPosts = db.relationship('favPosts', backref='users')

    def __init__(self, username, email, password, logo=None):
        self.username = username
        self.email = email
        self.password = password
        self.logo = logo
        db.session.add(self)
        db.session.commit()

    def loginning(email, password):
        user = Users.query.filter_by(email=email, password=password).first()
        try:
            return [user.username, user.email]
        except AttributeError: 
            return None

    def update_psw(email, new_password):
        user = Users.query.filter_by(email=email).first()
        user.password = new_password
        db.session.commit()

    def return_user_to_db(email):
        user = Users.query.filter_by(email=email).first()
        return user

def registration(username, email, password):
    user = Users.query.filter_by(email=email).first()
    if type(user) == NoneType:
        user = Users(username=username, email=email, password=password)
        return f'Зарегестрирован новый пользователь {username}\nEmail: {email}'
    else:
        return 'Пользователь с таким Email уже существует!'

        
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_title = db.Column(db.String(100))
    phone_number = db.Column(db.Integer)
    category = db.Column(db.Integer)
    cost = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(8000), nullable=True)
    post_date = db.Column(db.DateTime)
    deactivate_date = db.Column(db.DateTime)
    whatsapp_link = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=False, nullable=False)
    advertisement = db.Column(db.Boolean, default=False, nullable=False)
    photo = db.relationship('Photos', backref='posts')
    favpost = db.relationship('favPosts', backref = 'posts')

    def __init__(self, user, post_title, phone_number, category, cost, description, post_date, deactivate_date, whatsapp_link, status, advertisement):
        self.user = user.id
        self.post_title = post_title
        self.phone_number = phone_number
        self.category = category
        self.cost = cost
        self.description = description
        self.post_date = post_date
        self.deactivate_date = deactivate_date
        self.whatsapp_link = whatsapp_link
        self.status = status
        self.advertisement = advertisement
        db.session.add(self)
        db.session.commit()

    def show_all_posts():
        posts = Posts.query.order_by(Posts.post_date).filter_by(status=True).all()
        postss = []
        for i in range(len(posts)):
            id = posts[i].id
            title = posts[i].post_title
            phone_number = posts[i].phone_number
            category = posts[i].category
            cost = posts[i].cost
            description = posts[i].description
            post_date = posts[i].post_date.strftime("%m/%d/%Y %H:%M")
            deactivate_date = posts[i].deactivate_date.strftime("%m/%d/%Y %H:%M")
            whatsapp_link = posts[i].whatsapp_link
            advertisement = posts[i].advertisement
            photos = []
            for j in range(len(posts[i].photo)):
                photos.append(base64.b64encode(posts[i].photo[j].data).decode('ascii'))
            postss.append({'id':id, 'title': title, 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date, 'deactivate_date':deactivate_date, 'whatsapp_link':whatsapp_link, 'photos':photos, 'advertisement':advertisement})
        postss.reverse()
        return postss

    def show_posts_of_user(email):
        user = Users.query.filter_by(email=email).first()
        user_id = user.id
        posts = Posts.query.filter_by(user=user_id).all()
        postss = []
        for i in range(len(posts)):
            id = posts[i].id
            title = posts[i].post_title
            phone_number = posts[i].phone_number
            category = posts[i].category
            cost = posts[i].cost
            description = posts[i].description
            post_date = posts[i].post_date.strftime("%m/%d/%Y %H:%M")
            deactivate_date = posts[i].deactivate_date.strftime("%m/%d/%Y %H:%M")
            whatsapp_link = posts[i].whatsapp_link
            status = posts[i].status
            photos = []
            for j in range(len(posts[i].photo)):
                photos.append(base64.b64encode(posts[i].photo[j].data).decode('ascii'))
            postss.append({'id':id, 'title': title, 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date, 'deactivate_date':deactivate_date, 'whatsapp_link':whatsapp_link, 'status':status, 'photos':photos})
        postss.reverse()
        return postss

    def show_one_post(post_id):
        posts = Posts.query.filter_by(id=post_id).first()
        id = posts.id
        user_id = posts.user
        user = Users.query.filter_by(id = user_id).first()
        username = user.username
        title = posts.post_title
        phone_number = posts.phone_number
        category = posts.category
        cost = posts.cost
        description = posts.description
        post_date = posts.post_date.strftime("%m/%d/%Y %H:%M")
        deactivate_date = posts.deactivate_date
        whatsapp_link = posts.whatsapp_link
        photos = []
        for j in range(len(posts.photo)):
            photos.append(base64.b64encode(posts.photo[j].data).decode('ascii'))
        post = {'id':id, 'title': title, 'username':username, 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date, 'deactivate_date':deactivate_date, 'whatsapp_link':whatsapp_link, 'photos':photos}
        return post

    def post_activation(post_id):
        posts = Posts.query.filter_by(id=post_id).first()
        posts.status = True
        posts.post_date = datetime.today()
        posts.deactivate_date = datetime.today() + timedelta(days=14)
        db.session.commit()

    def post_to_vip(post_id):
        posts = Posts.query.filter_by(id=post_id).first()
        posts.advertisement = True
        db.session.commit()
    

    def post_deactivation(today):
        posts = Posts.query.order_by(Posts.deactivate_date).all()
        for i in posts:
            if posts[i.id-1].deactivate_date <= today:
                posts[i.id-1].status = False
                db.session.commit()

    def post_deactivayion_by_user(post_id):
        posts = Posts.query.filter_by(id = post_id).first()
        print(posts)
        posts.status = False
        db.session.commit()
      



class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __init__(self, data, post_id):
        self.data = data
        self.post_id = post_id.id
        db.session.add(self)
        db.session.commit()

class favPosts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    
    def __init__(self, user_id, post_id):
        self.user_id = user_id
        self.post_id = post_id
        db.session.add(self)
        db.session.commit()

    def show_favPosts(user_id):
        posts = favPosts.query.filter_by(user_id=user_id).all()
        postss = []
        for i in range(len(posts)):
            postss.append(Posts.show_one_post(posts.id))                   
        return postss


# print(Posts.show_posts_of_user('dakee088@gmail.com'))
# След. шаг: Выводить в пост его данные + фотографии
# Данные для поста: 
# Photos, user, title, phone_number, category, cost, description, post_date, link