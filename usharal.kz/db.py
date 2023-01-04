import base64
from datetime import datetime, timedelta
from types import NoneType
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
    phone_number = db.Column(db.Integer, nullable = True)
    photo = db.relationship('Posts', backref='users')
    favPosts = db.relationship('favPosts', backref='users')

    def __init__(self, username, email, password, logo=None, phone_number=None):
        self.username = username
        self.email = email
        self.password = password
        self.logo = logo
        self.phone_number = phone_number
        db.session.add(self)
        db.session.commit()

    def return_user_password(user_email):
        user = Users.query.filter_by(email = user_email).first()
        return user.password

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

    def show_user_information(email):
        user = Users.query.filter_by(email=email).first()
        email = user.email
        username = user.username
        if user.logo != None:
            logo = base64.b64encode(user.logo).decode('ascii')  
        else:
            logo = 0
        if user.phone_number != None:
            phone_number = user.phone_number
        else: 
            phone_number = 0
        return ({'email':email, 'username':username, 'logo':logo, 'phone_number':phone_number})

    def edit_user_information(email, logo, phone_number, password, username):
        user = Users.query.filter_by(email=email).first()
        print(type(password))
        if logo != b'':
            user.logo = logo
        if phone_number != '':
            user.phone_number = phone_number
        if password != '':
            user.password = password
        if username != '':
            user.username = username
        db.session.commit()

    def return_user_logo(user_id):
        user = Users.query.filter_by(id = user_id).first()
        if user.logo != None:
            logo = base64.b64encode(user.logo).decode('ascii')
            return logo
        else:
            return 0

    def return_user_id(user_email):
        user = Users.query.filter_by(email = user_email).first()
        return user.id

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
    delete_date = db.Column(db.DateTime)
    whatsapp_link = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=False, nullable=False)
    advertisement = db.Column(db.Boolean, default=False, nullable=False)
    view_counter = db.Column(db.Integer)
    fav_counter = db.Column(db.Integer)
    facility = db.Column(db.Integer)
    photo = db.relationship('Photos', backref='posts')
    favpost = db.relationship('favPosts', backref = 'posts')


    def __init__(self, user, post_title, phone_number, category, cost, description, post_date, deactivate_date, delete_date, whatsapp_link, status, advertisement, facility):
        self.user = user.id
        self.post_title = post_title
        self.phone_number = phone_number
        self.category = category
        self.cost = cost
        self.description = description
        self.post_date = post_date
        self.deactivate_date = deactivate_date
        self.delete_date = delete_date
        self.whatsapp_link = whatsapp_link
        self.status = status
        self.advertisement = advertisement
        self.facility = facility
        self.view_counter = 0
        self.fav_counter = 0
        db.session.add(self)
        db.session.commit()




    def edit_post(id, user, post_title, phone_number, category, cost, description, post_date, deactivate_date, delete_date, whatsapp_link, status, advertisement, facility):
        post = Posts.query.filter_by(id = id).first()
        post.user = user
        post.post_title = post_title
        post.phone_number = phone_number
        post.category = category
        post.cost = cost
        post.description = description
        post.post_date = post_date
        post.deactivate_date = deactivate_date
        post.delete_date = delete_date
        post.whatsapp_link = whatsapp_link
        post.status = status
        post.advertisement = advertisement
        post.facility = facility

    def show_all_posts():
        posts = Posts.query.order_by(Posts.post_date).filter_by(status=True).all()
        postss = []
        for i in range(len(posts)):
            id = posts[i].id
            title = posts[i].post_title
            phone_number = posts[i].phone_number
            if posts[i].category == 1:
                category = 'Услуги'
            elif posts[i].category == 2:
                category = 'Электроника'
            elif posts[i].category == 3:
                category = 'Личные вещи'
            elif posts[i].category == 4:
                category = 'Детям'
            elif posts[i].category == 5:
                category = 'Для бизнеса'
            elif posts[i].category == 6:
                category = 'Животные'
            elif posts[i].category == 7:
                category = 'Для дома'
            elif posts[i].category == 8:
                category = 'Работа'
            elif posts[i].category == 9:
                category = 'Хобби и спорт'
            elif posts[i].category == 10:
                category = 'Недвижимость'
            elif posts[i].category == 11:
                category = 'Транспорт'

            cost = posts[i].cost
            description = posts[i].description
            post_date = posts[i].post_date.strftime("%m/%d/%Y %H:%M")
            deactivate_date = posts[i].deactivate_date.strftime("%m/%d/%Y %H:%M")
            delete_date = posts[i].delete_date.strftime("%m/%d/%Y %H:%M")
            whatsapp_link = posts[i].whatsapp_link
            advertisement = posts[i].advertisement
            facility = posts[i].facility
            if facility == 1:
                facility = "Цена"
            elif facility == 2:
                facility = 'Возможен обмен'
            elif facility == 3:
                facility = 'Отдам даром'
            try:
                photos = base64.b64encode(posts[i].photo[0].data).decode('ascii')
            except:
                photos = 0
            postss.append({'id':id, 'title': title, 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date, 'deactivate_date':deactivate_date, "delete_date":delete_date, 'whatsapp_link':whatsapp_link, 'photos':photos, 'advertisement':advertisement, 'facility':facility})
        postss.reverse()
        return postss

    def category_filter(category):
        posts = Posts.query.filter_by(category=category).all()
        postss = []
        for i in range(len(posts)):
            id = posts[i].id
            title = posts[i].post_title
            phone_number = posts[i].phone_number
            if posts[i].category == 1:
                category = 'Услуги'
            elif posts[i].category == 2:
                category = 'Электроника'
            elif posts[i].category == 3:
                category = 'Личные вещи'
            elif posts[i].category == 4:
                category = 'Детям'
            elif posts[i].category == 5:
                category = 'Для бизнеса'
            elif posts[i].category == 6:
                category = 'Животные'
            elif posts[i].category == 7:
                category = 'Для дома'
            elif posts[i].category == 8:
                category = 'Работа'
            elif posts[i].category == 9:
                category = 'Хобби и спорт'
            elif posts[i].category == 10:
                category = 'Недвижимость'
            elif posts[i].category == 11:
                category = 'Транспорт'
            cost = posts[i].cost
            description = posts[i].description
            post_date = posts[i].post_date.strftime("%m/%d/%Y %H:%M")
            deactivate_date = posts[i].deactivate_date.strftime("%m/%d/%Y %H:%M")
            delete_date = posts[i].delete_date.strftime("%m/%d/%Y %H:%M")
            whatsapp_link = posts[i].whatsapp_link
            status = posts[i].status
            facility = posts[i].facility
            if facility == 1:
                facility = "Цена"
            elif facility == 2:
                facility = 'Возможен обмен'
            elif facility == 3:
                facility = 'Отдам даром'
            try:
                photos = base64.b64encode(posts[i].photo[0].data).decode('ascii')
            except:
                photos = 0
            postss.append({'id':id, 'title': title, 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date, 'deactivate_date':deactivate_date, "delete_date":delete_date, 'whatsapp_link':whatsapp_link, 'status':status, "facility":facility, 'photos':photos})
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
            if posts[i].category == 1:
                category = 'Услуги'
            elif posts[i].category == 2:
                category = 'Электроника'
            elif posts[i].category == 3:
                category = 'Личные вещи'
            elif posts[i].category == 4:
                category = 'Детям'
            elif posts[i].category == 5:
                category = 'Для бизнеса'
            elif posts[i].category == 6:
                category = 'Животные'
            elif posts[i].category == 7:
                category = 'Для дома'
            elif posts[i].category == 8:
                category = 'Работа'
            elif posts[i].category == 9:
                category = 'Хобби и спорт'
            elif posts[i].category == 10:
                category = 'Недвижимость'
            elif posts[i].category == 11:
                category = 'Транспорт'
            cost = posts[i].cost
            description = posts[i].description
            post_date = posts[i].post_date.strftime("%m/%d/%Y %H:%M")
            deactivate_date = posts[i].deactivate_date.strftime("%m/%d/%Y %H:%M")
            delete_date = posts[i].delete_date.strftime("%m/%d/%Y %H:%M")
            whatsapp_link = posts[i].whatsapp_link
            status = posts[i].status
            view_counter = posts[i].view_counter
            fav_counter = posts[i].fav_counter
            facility = posts[i].facility
            if facility == 1:
                facility = "Цена"
            elif facility == 2:
                facility = 'Возможен обмен'
            elif facility == 3:
                facility = 'Отдам даром'
            try:
                photos = base64.b64encode(posts[i].photo[0].data).decode('ascii')
            except:
                photos = 0
            postss.append({'id':id, 'title': title, 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date, 'deactivate_date':deactivate_date, "delete_date":delete_date, 'whatsapp_link':whatsapp_link, 'status':status, "view_counter":view_counter, "fav_counter":fav_counter, "facility":facility, 'photos':photos})
        postss.reverse()
        return postss

    def show_one_post(post_id):
        posts = Posts.query.filter_by(id=post_id).first()
        posts.view_counter += 1
        db.session.commit()
        id = posts.id
        user_id = posts.user
        user = Users.query.filter_by(id = user_id).first()
        username = user.username
        title = posts.post_title
        phone_number = posts.phone_number
        if posts.category == 1:
                category = 'Услуги'
        elif posts.category == 2:
            category = 'Электроника'
        elif posts.category == 3:
            category = 'Личные вещи'
        elif posts.category == 4:
            category = 'Детям'
        elif posts.category == 5:
            category = 'Для бизнеса'
        elif posts.category == 6:
            category = 'Животные'
        elif posts.category == 7:
            category = 'Для дома'
        elif posts.category == 8:
            category = 'Работа'
        elif posts.category == 9:
            category = 'Хобби и спорт'
        elif posts.category == 10:
            category = 'Недвижимость'
        elif posts.category == 11:
            category = 'Транспорт'
        cost = posts.cost
        description = posts.description
        post_date = posts.post_date.strftime("%m/%d/%Y %H:%M")
        deactivate_date = posts.deactivate_date.strftime("%m/%d/%Y %H:%M")
        delete_date = posts.delete_date.strftime("%m/%d/%Y %H:%M")
        whatsapp_link = posts.whatsapp_link
        view_counter = posts.view_counter
        fav_counter = posts.fav_counter
        facility = posts.facility
        if facility == 1:
            facility = "Цена"
        elif facility == 2:
            facility = 'Возможен обмен'
        elif facility == 3:
            facility = 'Отдам даром'
        photos = []
        for j in range(len(posts.photo)):
            photos.append(base64.b64encode(posts.photo[j].data).decode('ascii'))
        post = {'id':id, 'user_id': user_id, 'title': title, 'username':username, 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date, 'deactivate_date':deactivate_date, "delete_date":delete_date, 'whatsapp_link':whatsapp_link, "view_counter":view_counter, "fav_counter":fav_counter, 'facility':facility, 'photos':photos}
        return post

    def show_several_posts(postsId_list):
        all_posts = []
        for id in postsId_list:
            post = Posts.query.filter_by(id = id).first()
            id = post.id
            user_id = post.user
            user = Users.query.filter_by(id = user_id).first()
            username = user.username
            title = post.post_title
            phone_number = post.phone_number
            category = post.category
            cost = post.cost
            description = post.description
            post_date = post.post_date.strftime("%m/%d/%Y %H:%M")
            deactivate_date = post.deactivate_date.strftime("%m/%d/%Y %H:%M")
            delete_date = post.delete_date.strftime("%m/%d/%Y %H:%M")
            whatsapp_link = post.whatsapp_link
            facility = post.facility
            if facility == 1:
                facility = "Цена"
            elif facility == 2:
                facility = 'Возможен обмен'
            elif facility == 3:
                facility = 'Отдам даром'
            try:
                photos = base64.b64encode(post.photo[0].data).decode('ascii')
            except:
                photos = 0
            post_main = {'id':id, 'title': title, 'username':username, 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date, 'deactivate_date':deactivate_date, "delete_date":delete_date, 'whatsapp_link':whatsapp_link, 'facility':facility, 'photos':photos}
            all_posts.append(post_main)
        return all_posts

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

    def post_deactivation_by_user(post_id):
        posts = Posts.query.filter_by(id = post_id).first()
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

    def show_favPosts(user_email):
        user = Users.query.filter_by(email=user_email).first()
        user_id = user.id
        posts = favPosts.query.filter_by(user_id=user_id).all()
        postsId = []
        for i in posts:
            postsId.append(i.post_id)
        return Posts.show_several_posts(postsId)
    
    def checkUserFavPosts(user_email, post_id):
        user = Users.query.filter_by(email=user_email).first()
        user_id = user.id
        favPost = favPosts.query.filter_by(user_id=user_id).all()
        posts = []
        for i in favPost:
            posts.append(i.post_id)
        if post_id in posts:
            checker = False
        else:
            checker = True
        return checker
       
    def add_favPost(user_email, post_id):
        post_id = int(post_id)
        user = Users.query.filter_by(email=user_email).first()
        user_id = user.id
        checker = favPosts.checkUserFavPosts(user_email, post_id)
        post = Posts.query.filter_by(id = post_id).first()
        post.fav_counter += 1
        if checker:
            favPost = favPosts(user_id, post_id)
            db.session.add(favPost)
            db.session.commit()
        else:
            pass

    def delete_favPost(user_email, post_id):
        post_id=int(post_id)
        user = Users.query.filter_by(email=user_email).first()
        user_id = user.id
        post = Posts.query.filter_by(id = post_id).first()
        post.fav_counter -= 1
        post_delete = favPosts.query.filter_by(user_id=user_id, post_id=post_id).first()
        db.session.delete(post_delete)
        db.session.commit()


    def give_favPostId_of_user(user_email):
        user = Users.query.filter_by(email=user_email).first()
        user_id = user.id
        posts_id = []
        posts = favPosts.query.filter_by(user_id=user_id).all()
        for post in posts:
            posts_id.append(post.post_id)
        return posts_id
