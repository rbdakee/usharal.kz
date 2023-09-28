import os
import uuid
# from types import NoneType
from flask import Flask, render_template, url_for, request, redirect, flash, session, abort, make_response, jsonify
from itsdangerous import URLSafeTimedSerializer
import itsdangerous
from send_email import send_link
from datetime import datetime, timedelta, timezone
from db import *
from flask_socketio import SocketIO, emit


app = Flask(__name__)
s = URLSafeTimedSerializer('alshdawdowg1288faklsf7fgasbfawfasdawfavxvdzwasdw2')
app.config["SECRET_KEY"] = 'jp0?ad[1-=-0-`94mpgf-pjmwr3;2owdakdnw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)
socketio = SocketIO(app, cors_allowed_origins='*', async_mode="gevent", ping_timeout=30, ping_interval=20)
with app.app_context():
    db.create_all()


menu = [{'name': 'Сообщения', 'url': "messages"},
        {'name': 'Мои объявления', 'url': 'mypost'},
        {'name': 'Платежи и счет', 'url': 'payments'},
        {'name': 'Мой профиль', 'url': 'myprofile'},
        {'name': 'Выход', 'url': 'logout'},]
dataCat = {
            1: 'Услуги',
            2: 'Электроника',
            3: 'Личные вещи',
            4: 'Детям',
            5: 'Для Бизнеса',
            6: 'Животные', 
            7: 'Для дома',
            8: 'Работа',
            9: 'Хобби и спорт',
            10: 'Недвижимость',
            11: 'Транпорт'
        }
catData = {
            'Все категории': 0,
            'Услуги':1,
             'Электроника':2,
             'Личные вещи':3,
             'Детям':4,
             'Для Бизнеса':5,
             'Животные':6, 
             'Для дома':7,
             'Работа':8,
            'Хобби и спорт':9,
            'Недвижимость':10,
            'Транспорт':11
        }
dictValues = {
    'Услуги': 'lng-service',
    'Электроника' :'lng-gadgets',
    'Личные вещи' : 'lng-personalItems',
    'Детям' : 'lng-child',
    'Для Бизнеса' : 'lng-business',
    'Животные' : 'lng-animals',
    'Для Дома' : 'lng-house',
    'Работа' : 'lng-job',
    'Хобби и спорт' : 'lng-hobby',
    'Недвижимость' : 'lng-apartments',
    'Транспорт' : 'lng-transport',
    'Договорная цена': 'lng-dogov',
    'Цена': 'lng-cost',
    'Отдам даром': 'lng-free',
    'Возможен обмен': 'lng-swap',
    'Все категории':'lng-categories',
    'Договорная':'lng-contract'
}

arrLang = []
arrLang2 = []
category = 0
title='úsharal'
@app.route('/', methods=['POST', 'GET'])
@app.route('/<lang>', methods=['POST', 'GET'])
def index(lang='ru'):
    if lang != 'ru' and lang != 'kz':
        lang = 'ru'
        return redirect(url_for('index', lang = 'ru'))
    arrLang.append(lang)
    arrLang2 = [i for i in arrLang if i != 'favicon.ico']
    Posts.post_deactivation(today = datetime.today())
    if request.cookies.get('userName') and request.cookies.get('userEmail'):
        session['userName'] = request.cookies.get('userName')
        session['userEmail'] = request.cookies.get('userEmail')

    session['lang'] = arrLang2[-1]
    arrLang.clear()
    arrLang2.clear()
    if request.method == 'POST' or request.method == 'GET':

        if request.method == 'GET':
            data = request.args.get('category')
            search = request.args.get('search-field')
            if data:
                category = catData[data]
            else:
                category = 0
            if category!=0:
                if search:
                    posts = Posts.search_posts(request.args.get('search-field'), category)
                else:
                    posts = Posts.category_filter(category)
            elif search:
                posts = Posts.search_posts(request.args.get('search-field'), 0)
            else:
                posts = Posts.show_all_posts()
                data = 'Все категории'
        else:
            posts = Posts.show_all_posts()
            data = 'Все категории'
        if 'userEmail' in session:
            try:
                favPost = favPosts.give_favPostId_of_user(session['userEmail'])
                return render_template('index.html',title = title, menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], favourites = favPost, category = data, cat = dictValues, lenOfUserName = len(session['userName']))
            except AttributeError:
                session.pop('userEmail', None)
                session.pop('userName', None)
                request
                return redirect(url_for('index', lang = session['lang'] ))
        else:
            return render_template('index.html',title = title, menu = menu, username=f'Log In', uuurl='signin', posts = posts, lang = session['lang'], category = data, cat = dictValues, lenOfUserName = 1)
    if 'userEmail' in session:
        posts = Posts.show_all_posts()
        try:
            favPost = favPosts.give_favPostId_of_user(session['userEmail'])
            return render_template('index.html',title = title, menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], favourites = favPost, category = 'Все категории', cat = dictValues, lenOfUserName = len(session['userName']))
        except AttributeError:
            session.pop('userEmail', None)
            session.pop('userName', None)
            return redirect(url_for('index', lang = session['lang'] ))
    else:
        posts = Posts.show_all_posts()
        return render_template('index.html',title = title, menu = menu, username=f'Log In', uuurl='signin', posts = posts, lang = session['lang'], category = 'Все категории', cat = dictValues, lenOfUserName = 1)
    

@socketio.on('favPost')
def echo(data):
    print(data)
    userEmail = session['userEmail']
    value = data['value']
    classes = data['class']
    if 'fa-regular' in classes.values():
        favPosts.add_favPost(userEmail, value)
    elif 'fa' in classes.values():
        favPosts.delete_favPost(userEmail, value)


# My Route for CHAT.HTML
@app.route('/chat/<int:pk>/<lang>', methods=['POST', 'GET'])
def chat(lang, pk):
    if 'userEmail' in session:
        if lang != 'ru' and lang != 'kz':
            lang = 'ru'
            return redirect(url_for('chat', lang = 'ru'))
        
        if request.method=='POST':
            message_content = request.form.get('textarea_message')
            receiver_id = pk
            sender_id = Users.return_user_id(session['userEmail'])
            message = Message(content=message_content, sender_id=sender_id, receiver_id=receiver_id)
            db.session.add(message)
            db.session.commit()


        session['lang'] = lang
        sender_id = Users.return_user_id(session['userEmail'])
        buddyEmail = Users.return_user_email_by_id(pk)
        buddy_logo = Users.return_user_logo(pk)
        buddy_info = Users.show_user_information(buddyEmail)


        chat_history_by_date = Message.get_chat_history(sender_id, pk)

        return render_template('chat.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), messages_by_date=chat_history_by_date, this_user_id=str(sender_id), buddy_logo=buddy_logo, buddy_info=buddy_info, buddy_id = str(pk))
    else:
        return redirect(url_for('login', lang=lang))

@app.route('/messages/<lang>')
def messages(lang):
    if 'userEmail' in session:
        if lang != 'ru' and lang != 'kz':
            lang = 'ru'
            return redirect(url_for('messages', lang = 'ru'))
        session['lang'] = lang
        sender_id = Users.return_user_id(session['userEmail'])
        chats = Message.get_chatted_users_with_last_message(sender_id)
        return render_template('messages.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), chats = chats)
    else:
        return redirect(url_for('login', lang=lang))
    
@socketio.on('message')
def handle_message(data):
    message_content = data['message']
    sender_id = Users.return_user_id(session['userEmail'])
    receiver_id = data['receiver_id']
    message = Message(content=message_content, sender_id=sender_id, receiver_id=receiver_id)
    db.session.add(message)
    db.session.commit()

    emit('message', data, broadcast=True)

@app.route('/my_profile/<lang>', methods=['POST', 'GET'])
def myprofile(lang='ru'):
    if 'userEmail' in session:
        booleanValue = 0
        userpass = Users.return_user_password(session['userEmail'])
        if request.method == 'POST':
            prevpass = request.form['userPrevPassword']
            if prevpass == userpass: 
                username = request.form['username']
                session['userName'] = username
                img = request.files['logo']
                if img.filename != '':
                    filename = upload_image(img)
                    logo = filename         
                else:
                    logo = ''           
                whatsapp_number = request.form['whatsapp_number']
                phone_number = request.form['phone_number']
                password = request.form['password']
                Users.edit_user_information(email=session['userEmail'], logo=logo, whatsapp_number=whatsapp_number, phone_number=phone_number, password=password, username=username)
            else:
                flash('Неверный пароль')
                booleanValue = 1
                user_information = Users.show_user_information(session['userEmail'])
                return render_template('profile.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', user = user_information, lang=session['lang'], lenOfUserName = len(session['userName']), value = booleanValue)
        session['lang'] = lang
        user_information = Users.show_user_information(session['userEmail'])
        return render_template('profile.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', user = user_information, lang=session['lang'], lenOfUserName = len(session['userName']), value = booleanValue)
    else:
        return redirect(url_for('login', lang=lang))

@app.route('/my_posts/<lang>')
def myposts(lang):
    a_token = s.dumps( session['userEmail'], salt='post-activation' )
    d_token = s.dumps( session['userEmail'], salt='post-deactivation' )
    Posts.post_deactivation(today = datetime.today())
    if 'userEmail' in session:
        session['lang'] = lang
        if lang != 'ru' and lang != 'kz':
            lang = 'ru'
            return redirect(url_for('myposts', lang = 'ru'))
        posts = Posts.show_posts_of_user(session['userEmail'])
        return render_template('my-posts.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], cat = dictValues, lenOfUserName = len(session['userName']), a_token=a_token, d_token=d_token)
    else:  
        return redirect(url_for('login', lang=lang))

def phone_numbers_to_waLink(number):
    res = ''
    for i in number:
        if i in '1234567890':
            res+=i
    return res

boolclicked = [-1]
def generate_unique_filename(filename):
    extension = filename.rsplit('.', 1)[1] if '.' in filename else 'jpg'
    unique_filename = str(uuid.uuid4()) + '.' + extension
    return unique_filename

def upload_image(file):
    if file:
        filename = generate_unique_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return filename
    return None

@app.route('/new_post/<lang>', methods=['POST', 'GET'])
def newpost(lang):
    if 'userName' in session:
        user_is = Users.show_user_information(session['userEmail'])
        if lang != 'ru' and lang != 'kz':
            lang = 'ru'
            return redirect(url_for('newpost', lang = 'ru'))
        session['lang'] = lang
        if request.method == 'POST':
            if 'photo_from_review' not in request.form:
                user = Users.return_user_to_db(session['userEmail'])
                email = request.form['user_email']
                post_title=request.form['post_title']
                category=request.form['category']
                cost = request.form['post_cost']
                photo = request.files.getlist('post_photo')[0:8]
                description = request.form['post_description']
                phone_number = request.form['phone_number']
                whatsapp_phone_number = request.form['whatsapp_phone_number']
                whatsapp_link = f'https://wa.me/{phone_numbers_to_waLink(whatsapp_phone_number)}'
                deactivate_date = datetime.today() + timedelta(days=14)
                delete_date = deactivate_date + timedelta(days=14)
                location = request.form['post_location']
                email = request.form['user_email']
                status = True
                advertisement = False
                facility = request.form['radio']
                post_date = datetime.today()
                post = Posts(user, post_title, phone_number, category, cost, description, post_date, deactivate_date, delete_date, whatsapp_link, status, advertisement, facility, email, location)
                for uploaded_file in photo:
                    if uploaded_file.filename != '':
                        filename = upload_image(uploaded_file)
                        if filename:
                            image = Photos(filename, post.id)        
                return redirect(url_for('index', lang = session['lang']))
            else:
                user = Users.return_user_to_db(session['userEmail'])
                post_title=request.form['post_title']
                category=request.form['category']
                cost = request.form['post_cost']
                photo = request.form['photos_from_review']
                description = request.form['post_description']
                location = request.form['post_location']
                phone_number = request.form['phone_number']
                whatsapp_phone_number = request.form['whatsapp_phone_number']
                email = request.form['user_email']            
                post = {"user":user, "post_title":post_title, "phone_number":phone_number, "category":category, "cost":cost, "description":description, "photos":photo, 'location':location}
                return render_template('new-post.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), phone_number=user_is['phone_number'], whatsapp_number = user_is['whatsapp_number'], bc = boolclicked[-1], post=post)


        return render_template('new-post.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), phone_number=user_is['phone_number'], whatsapp_number = user_is['whatsapp_number'], bc = boolclicked[-1])
    else:
        return redirect(url_for('login', lang=lang))

@app.route('/edit_post/<post_id>/<lang>', methods = ['POST', 'GET'])
def edit_post(post_id, lang):
    
    if request.method == 'POST':
        id = post_id
        user = Users.return_user_to_db(session['userEmail'])
        post_title=request.form['post_title']
        category=request.form['category']
        cost = request.form['post_cost']
        try:
            photo = request.files.getlist('post_photo')[0:10]
            if "''" in str(photo):
                photo = Photos.return_post_photos(post_id)
            else:
                photo = list(map(lambda x: x.read(), photo))
        except:
            photo = Photos.return_post_photos(post_id)

        description = request.form['post_description']
        location = request.form['post_location']
        phone_number = request.form['phone_number']
        whatsapp_phone_number = request.form['whatsapp_phone_number']
        whatsapp_link = f'https://wa.me/{phone_numbers_to_waLink(whatsapp_phone_number)}'
        deactivate_date = datetime.today() + timedelta(days=14)
        delete_date = deactivate_date + timedelta(days=14)
        status = True
        advertisement = False
        facility = request.form['radio']
        email = request.form['user_email']
        post_date = datetime.today()
        new_post = Posts.edit_post(id, user, post_title, phone_number, category, cost, description, post_date, deactivate_date, delete_date, whatsapp_link, status, advertisement, facility, email=email, location=location)
        Photos.edit_photos(photo, id)
        return redirect(url_for('content', post_id=id, lang=session['lang']))
    post = Posts.show_one_post(post_id)
    if lang != 'ru' and lang != 'kz':
        lang = 'ru'
        return redirect(url_for('newpost', lang = 'ru'))
    if post['userEmail']!=session['userEmail']:
        abort(404)
    session['lang'] = lang
    lenOfPostPhotos = len(post['photos'])
    post['whatsapp_link'] = post['whatsapp_link'].split('/')[-1]
    other = 7- lenOfPostPhotos
    return render_template('edit_post.html', post = post, menu = menu, username=session['userName'], uuurl='myprofile', lenOfUserName = len(session['userName']), lang = session['lang'], lenOfPostPhotos = lenOfPostPhotos, other = other, title=title)

dictType = {
            '1': 'Услуги',
            '2': 'Электроника',
            '3': 'Личные вещи',
            '4': 'Детям',
            '5': 'Для Бизнеса',
            '6': 'Животные',
            '7': 'Для Дома',
            '8': 'Работа',
            '9': 'Хобби и спорт',
            '10': 'Недвижимость',
            '11': 'Транспорт',
        }

@app.route('/content/<post_id>/<lang>')
def content(post_id, lang):
    Posts.post_deactivation(today = datetime.today())
    if lang != 'ru' and lang != 'kz':
        lang = 'ru'
        return redirect(url_for('content', lang = 'ru'))
    session['lang'] = lang
    post = Posts.show_one_post(post_id)
    data = post['category']
    category = catData[data]
    user_logo = Users.return_user_logo(post['user_id'])
    related_posts = Posts.category_filter(category)
    len_of_rel_posts = len(related_posts)
    lngFacility = dictValues[post['facility']]
    if 'userEmail' in session:
        favPost = favPosts.give_favPostId_of_user(session['userEmail'])
        return render_template('profiletovara.html', post = post, menu=menu, title=title, username = session['userName'], uuurl='myprofile', related_posts = related_posts, lang = session['lang'], user_logo = user_logo, favourites = favPost, len_of_rel_posts = len_of_rel_posts, lenOfUserName = len(session['userName']), review = False, cat = dictValues, lngFacility=lngFacility)
    else:
        return render_template('profiletovara.html', username = 'Log In', lang = session['lang'], post = post, menu=menu, title=title, uuurl='myprofile', related_posts = related_posts, user_logo = user_logo, len_of_rel_posts = len_of_rel_posts, lenOfUserName = 1, review = False, cat = dictValues, lngFacility=lngFacility)

@app.route('/post_activation/<post_id>/<a_token>/<lang>')
def activation(post_id, a_token, lang):
    try:
        s.loads(a_token, salt='post-activation', max_age=60)
    except (itsdangerous.exc.SignatureExpired, itsdangerous.exc.BadTimeSignature, itsdangerous.exc.BadSignature):
        return render_template('expired_token.html')
    if lang != 'ru' and lang != 'kz':
        lang = 'ru'
        return redirect(url_for('myposts', lang = 'ru'))
    post_id = int(post_id)
    Posts.post_activation(post_id)
    return redirect(url_for('myposts', lang = session['lang']))

@app.route('/post_deactivation/<post_id>/<d_token>/<lang>')
def deactivation(post_id, d_token, lang):
    try:
        s.loads(d_token, salt='post-deactivation', max_age=60)
    except (itsdangerous.exc.SignatureExpired, itsdangerous.exc.BadTimeSignature, itsdangerous.exc.BadSignature):
        return render_template('expired_token.html')
    if lang != 'ru' and lang != 'kz':
        lang = 'ru'
        return redirect(url_for('myposts', lang = 'ru'))
    session['lang'] = lang
    post_id = int(post_id)
    Posts.post_deactivation_by_user(post_id)
    return redirect(url_for('myposts', lang = session['lang']))

@app.route('/vippurchase/<post_id>')
def vippurchase(post_id):
    post_id = int(post_id)
    Posts.post_to_vip(post_id)
    return redirect(url_for('index'))

@app.route('/payments/<lang>')
def payments(lang):
    if 'userEmail' in session:
        if lang != 'ru' and lang != 'kz':
            lang = 'ru'
            return redirect(url_for('payments', lang = 'ru'))
        session['lang'] = lang
        return render_template('transaction.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login', lang=lang))

photo_inf = []
@app.route('/review/<post_id>/<lang>', methods = ["POST", 'GET'])
def review(lang, post_id = 0):
    
    if lang != 'ru' and lang != 'kz':
        lang = 'ru'
    session['lang'] = lang
    if request.method == 'POST':
        
        if post_id == 0:
            user = Users.return_user_to_db(session['userEmail'])
            post_title=request.form['post_title']
            category=request.form['category']
            cost = request.form['post_cost']
            photo = request.files.getlist('post_photo')[0:8]
            description = request.form['post_description']
            phone_number = request.form['phone_number']
            whatsapp_phone_number = request.form['whatsapp_phone_number']
            whatsapp_link = f'https://wa.me/{phone_numbers_to_waLink(whatsapp_phone_number)}'
            deactivate_date = datetime.today() + timedelta(days=14)
            status = True
            advertisement = False
            facility = request.form['radio']
            post_date = datetime.today()
            photo_inf = []
            for uploaded_file in photo:
                if uploaded_file.filename != '':
                    filename = upload_image(uploaded_file)
                    photo_inf.append(filename)   
            if facility == "1":
                facility_inf = 'Цена'
            elif facility == "2":
                facility_inf = 'Возможен обмен'
            elif facility == "3":
                facility_inf = 'Отдам даром'
            elif facility == '4':
                facility_inf = 'Договорная'

            post_inf = {'title': post_title, 'username':session['userName'], 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date.strftime("%m/%d/%Y %H:%M"), 'whatsapp_link':whatsapp_link, 'facility':facility_inf, 'photos':photo_inf}
            user_logo = Users.return_user_logo(Users.return_user_id(session['userEmail']))
            return render_template('profiletovara.html', post = post_inf, menu=menu, title=title, username = session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), review = True, cat = dictValues, user_logo=user_logo, photo = photo)
        else:
            
            user = Users.return_user_to_db(session['userEmail'])
            post_title=request.form['post_title']
            category=request.form['category']
            cost = request.form['post_cost']
            try:
                photo = request.files.getlist('post_photo')[0:10]
                if "''" in str(photo):
                    photo = Photos.return_post_photos(post_id)
                else:
                    photo = list(map(lambda x: x.read(), photo))
            except:
                photo = Photos.return_post_photos(post_id)

            description = request.form['post_description']
            phone_number = request.form['phone_number']
            whatsapp_phone_number = request.form['whatsapp_phone_number']
            whatsapp_link = f'https://wa.me/{phone_numbers_to_waLink(whatsapp_phone_number)}'
            deactivate_date = datetime.today() + timedelta(days=14)
            status = True
            advertisement = False
            facility = request.form['radio']
            post_date = datetime.today()
            photo_inf = []
            for uploaded_file in photo:
                if uploaded_file.filename != '':
                    filename = upload_image(uploaded_file)
                    photo_inf.append(filename) 
            if facility == "1":
                facility_inf = 'Цена'
            elif facility == "2":
                facility_inf = 'Возможен обмен'
            elif facility == "3":
                facility_inf = 'Отдам даром'
            elif facility == '4':
                facility_inf = 'Договорная'

            post_inf = {'title': post_title, 'username':session['userName'], 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date.strftime("%m/%d/%Y %H:%M"), 'whatsapp_link':whatsapp_link, 'facility':facility_inf, 'photos':photo_inf}
            user_logo = Users.return_user_logo(Users.return_user_id(session['userEmail']))
    return render_template('profiletovara.html', post = post_inf, menu=menu, title=title, username = session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), review = True, cat = dictValues, user_logo=user_logo)



@app.route('/favorites/<lang>', methods = ['POST', 'GET'])
def favorites(lang):
    Posts.post_deactivation(today = datetime.today())
    if 'userEmail' in session:
        if lang != 'ru' and lang != 'kz':
            lang = 'ru'
            return redirect(url_for('', lang = 'ru'))
        session['lang'] = lang
        posts = favPosts.show_favPosts(session['userEmail'])
        if request.args.get('search_field'):
            search_data = request.args.get('search_field')
            posts = posts = favPosts.show_favPosts(session['userEmail'], search_data)
        return render_template('izbrannoe.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], cat = dictValues, dictType = dictType, dataCat = dataCat, lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login', lang=lang))
           

@app.route('/signin/<lang>', methods = ['POST', 'GET'])
def login(user=None, lang='ru'):
    if request.method == 'POST':  
        if 'email' in request.form:
            user = Users.loginning(email=request.form['email'].lower(), password=request.form['password'])
            if user==None:
                flash("Неправильный логин или пароль! Повторите попытку.")
            elif type(user)==list:
                session['userName']=user[0]
                session['userEmail']=user[1]
                session.permanent = True
                session.permanent_session_lifetime = timedelta(days=3)
                return redirect(url_for('index', lang=lang))
        elif 'newemail' in request.form:
            user = registration(username=request.form['newuname'], email=request.form['newemail'].lower(), password=request.form['newpassword'])
            flash(user, 'h')
    
    return render_template('registration-login.html', title = title, lang=lang)

    

@app.route('/logout')
def logout():
    Posts.post_deactivation(today = datetime.today())
    session.pop('userEmail', None)
    session.pop('userName', None)
    return redirect(url_for('index', lang = session['lang'] ))

@app.route('/forgot', methods=['POST','GET'])
def xlogin():
    if request.method=="POST":
        try:
            user_email = request.form['forgot_email']
            token = s.dumps(user_email, salt='email-confirm')
            message = f'Это письмо было отправлено для сброса пароля на сайте usharal.market пользователя с электронным адресом "{user_email}"\nЕсли вы не хотите изменять пароль, не открывайте ссылку и не отправляйте ее никому\n' + url_for('confirm_email', token=token, email=user_email, _external=True)
            send_link(message, user_email)
            flash(f'Письмо было отправлено на почту {user_email}', 'success')
        except:
            flash('Что-то пошло не так, пожалуйста повторите попытку', 'red')

    return render_template('registration-login.html', title = title)

@app.route('/confirm_email/<token>/<email>')
def confirm_email(token, email):
    try:
        s.loads(token, salt='email-confirm', max_age=600)
    except (itsdangerous.exc.SignatureExpired, itsdangerous.exc.BadTimeSignature, itsdangerous.exc.BadSignature):
        return render_template('expired_token.html')
    return render_template('re.html', email = email)

@app.route('/update_password', methods=['POST', 'GET'])
def update_password():
    if request.method=='POST':
        new_password = request.form['newpassword']
        email = request.form['email']
        Users.update_psw(email.lower(), new_password)
        return redirect(url_for('login'))

@app.errorhandler(404)
def error_page(error):
    if 'userName' in session:
        return render_template('error_page.html', menu = menu, lang=session['lang'], lenOfUserName = len(session['userName']))
    else:
        return render_template('error_page.html', menu = menu, lang=session['lang'], lenOfUserName = 1)
    # return redirect(url_for('index', lang =))

@app.errorhandler(KeyError)
@app.errorhandler(AttributeError)
def attributeError_habdler(error):
    session.pop('userEmail', None)
    session.pop('userName', None)
    return redirect(url_for('index', lang = session['lang'] ))


if __name__ == '__main__':
    socketio.run(app, host='usharal.market', port=8000)
