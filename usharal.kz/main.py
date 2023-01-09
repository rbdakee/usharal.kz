import base64
from types import NoneType
from flask import Flask, render_template, url_for, request, redirect, flash, session, abort
from itsdangerous import URLSafeTimedSerializer
import itsdangerous
from send_email import send_link
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from db import Users, registration, Posts, Photos, favPosts
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)
s = URLSafeTimedSerializer('alshdawdowg1288faklsf7fgasbfawfasdawfavxvdzwasdw2')
app.config["SECRET_KEY"] = 'jp0?ad[1-=-0-`94mpgf-pjmwr3;2owdakdnw'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
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
    'Все категории':'lng-categories'
}
arrLang = []
arrLang2 = []
category = 0
title='usharal.kz'
@app.route('/', methods=['POST', 'GET'])
@app.route('/<lang>', methods=['POST', 'GET'])
def index(lang='rulang'):
    if lang != 'rulang' and lang != 'kzlang':
        lang = 'rulang'
        return redirect(url_for('index', lang = 'rulang'))
    arrLang.append(lang)
    arrLang2 = [i for i in arrLang if i != 'favicon.ico']
    Posts.post_deactivation(today = datetime.today())
    
    session['lang'] = arrLang2[-1]
    arrLang.clear()
    arrLang2.clear()
    if request.method == 'POST':
        data = request.form.get('category')
        if data == 'Услуги':
            category = 1
        elif data == 'Электроника':
            category = 2
        elif data == 'Личные вещи':
            category = 3
        elif data == 'Детям':
            category = 4
        elif data == 'Для Бизнеса':
            category = 5
        elif data == 'Животные':
            category = 6
        elif data == 'Для дома':
            category = 7
        elif data == 'Работа':
            category = 8
        elif data == 'Хобби и спорт':
            category = 9
        elif data == 'Недвижимость':
            category = 10
        elif data == 'Транспорт':
            category = 11
        
        posts = Posts.category_filter(category)
        if 'userEmail' in session:
            try:
                favPost = favPosts.give_favPostId_of_user(session['userEmail'])
                return render_template('index.html',title = title, menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], favourites = favPost, category = data, cat = dictValues, lenOfUserName = len(session['userName']))
            except AttributeError:
                session.pop('userEmail', None)
                session.pop('userName', None)
                return redirect(url_for('index', lang = session['lang'] ))
        else:
            return render_template('index.html',title = title, menu = menu, username=f'Log In', uuurl='authentification', posts = posts, lang = session['lang'], category = data, cat = dictValues, lenOfUserName = 1)
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
        return render_template('index.html',title = title, menu = menu, username=f'Log In', uuurl='authentification', posts = posts, lang = session['lang'], category = 'Все категории', cat = dictValues, lenOfUserName = 1)
    

@sock.route('/favPost')
def echo(sock):
    while True:
        data = sock.receive()
        userEmail = session['userEmail']
        data = data.split(',')
        print(data)
        classes = data[1].split()
        if 'fa-regular' in classes:
            favPost = favPosts.add_favPost(userEmail, data[0])
        elif 'fa' in classes:
            favPost = favPosts.delete_favPost(userEmail, data[0])
        sock.send(data)
@sock.route('/category')
def search_category(sock):
    while True:
        data = sock.receive().strip()   
        if data == 'Услуги':
            category = 1
        elif data == 'Электроника':
            category = 2
        elif data == 'Личные вещи':
            category = 3
        elif data == 'Детям':
            category = 4
        elif data == 'Для Бизнеса':
            category = 5
        elif data == 'Животные':
            category = 6
        elif data == 'Для дома':
            category = 7
        elif data == 'Работа':
            category = 8
        elif data == 'Хобби и спорт':
            category = 9
        elif data == 'Недвижимость':
            category = 10
        elif data == 'Транспорт':
            category = 11
        sock.send(category)


        


@app.route('/messages/<lang>')
def messages(lang):
    if 'userEmail' in session:
        if lang != 'rulang' and lang != 'kzlang':
            lang = 'rulang'
            return redirect(url_for('messages', lang = 'rulang'))
        session['lang'] = lang
        return render_template('messageSection.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login'))

@app.route('/myprofile/<lang>', methods=['POST', 'GET'])
def myprofile(lang='rulang'):
    if 'userEmail' in session:
        booleanValue = 0
        userpass = Users.return_user_password(session['userEmail'])
        if request.method == 'POST':
            prevpass = request.form['userPrevPassword']
            if prevpass == userpass: 
                username = request.form['username']
                session['userName'] = username
                logo = request.files['logo'].read()
                phone_number = request.form['phone_number']
                password = request.form['password']
                Users.edit_user_information(session['userEmail'], logo, phone_number, password, username)
            else:
                flash('Неверный пароль')
                booleanValue = 1
                user_information = Users.show_user_information(session['userEmail'])
                return render_template('myProfile.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', user = user_information, lang=session['lang'], lenOfUserName = len(session['userName']), value = booleanValue)
        session['lang'] = lang
        user_information = Users.show_user_information(session['userEmail'])
        return render_template('myProfile.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', user = user_information, lang=session['lang'], lenOfUserName = len(session['userName']), value = booleanValue)
    else:
        return redirect(url_for('login'))

@app.route('/mypost/<lang>')
def myposts(lang):
    a_token = s.dumps( session['userEmail'], salt='post-activation' )
    d_token = s.dumps( session['userEmail'], salt='post-deactivation' )
    Posts.post_deactivation(today = datetime.today())
    if 'userEmail' in session:
        session['lang'] = lang
        if lang != 'rulang' and lang != 'kzlang':
            lang = 'rulang'
            return redirect(url_for('myposts', lang = 'rulang'))
        posts = Posts.show_posts_of_user(session['userEmail'])
        return render_template('myPosts.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], cat = dictValues, lenOfUserName = len(session['userName']), a_token=a_token, d_token=d_token)
    else:  
        return redirect(url_for('login'))

def phone_numbers_to_waLink(number):
    res = ''
    for i in number:
        if i in '1234567890':
            res+=i
    return res

@sock.route('/post_photo')
def post_photo(sock):
    data = sock.receive()
    # print(data)

@app.route('/newpost/<lang>', methods=['POST', 'GET'])
def newpost(lang):
    if 'userName' in session:
        if lang != 'rulang' and lang != 'kzlang':
            lang = 'rulang'
            return redirect(url_for('newpost', lang = 'rulang'))
        session['lang'] = lang
        if request.method == 'POST':
            user = Users.return_user_to_db(session['userEmail'])
            post_title=request.form['post_title']
            category=request.form['category']
            cost = request.form['post_cost']
            photo = request.files.getlist('post_photo')
            # photo = request.form['absolute'].split()
            description = request.form['post_description']
            phone_number = request.form['phone_number']
            whatsapp_phone_number = request.form['whatsapp_phone_number']
            whatsapp_link = f'https://wa.me/{phone_numbers_to_waLink(whatsapp_phone_number)}'
            deactivate_date = datetime.today() + timedelta(days=14)
            delete_date = deactivate_date + timedelta(days=14)
            status = True
            advertisement = False
            facility = request.form['radio']
            post_date = datetime.today()
            post = Posts(user, post_title, phone_number, category, cost, description, post_date, deactivate_date, delete_date, whatsapp_link, status, advertisement, facility)
            if len(photo)>=9:
                for i in range(8):
                    photos = Photos(photo[i].read(), post)
            else:
                for i in photo:
                    photos = Photos(i.read(), post)
            
        return render_template('newPost.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), phone_number='+7 (777) 227-00-88', whatsapp_number = '+7 (777) 227-00-88')
    else:
        return redirect(url_for('login'))

@app.route('/edit_post/<post_id>/<lang>', methods = ['POST', 'GET'])
def edit_post(post_id, lang):
    post = Posts.show_one_post(post_id)
    if lang != 'rulang' and lang != 'kzlang':
        lang = 'rulang'
        return redirect(url_for('newpost', lang = 'rulang'))
    if post['userEmail']!=session['userEmail']:
        abort(404)
    session['lang'] = lang
    if request.method == 'POST':
        id = post_id
        user = Users.return_user_to_db(session['userEmail'])
        post_title=request.form['post_title']
        category=request.form['category']
        cost = request.form['post_cost']
        try:
            photo = request.files.getlist('post_photo')
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
        delete_date = deactivate_date + timedelta(days=14)
        status = True
        advertisement = False
        facility = request.form['radio']
        post_date = datetime.today()
        new_post = Posts.edit_post(id, user, post_title, phone_number, category, cost, description, post_date, deactivate_date, delete_date, whatsapp_link, status, advertisement, facility)
        Photos.edit_photos(photo, id)
        return redirect(url_for('content', post_id=id, lang=session['lang']))
    
    lenOfPostPhotos = len(post['photos'])
    post['whatsapp_link'] = post['whatsapp_link'].split('/')[-1]
    return render_template('editPost.html', post = post, menu = menu, username=session['userName'], uuurl='myprofile', lenOfUserName = len(session['userName']), lang = session['lang'], lenOfPostPhotos = lenOfPostPhotos)

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
    if lang != 'rulang' and lang != 'kzlang':
        lang = 'rulang'
        return redirect(url_for('content', lang = 'rulang'))
    session['lang'] = lang
    post = Posts.show_one_post(post_id)
    print(post['category'])
    data = post['category']
    if data == 'Услуги':
        category = 1
    elif data == 'Электроника':
        category = 2
    elif data == 'Личные вещи':
        category = 3
    elif data == 'Детям':
        category = 4
    elif data == 'Для Бизнеса':
        category = 5
    elif data == 'Животные':
        category = 6
    elif data == 'Для дома':
        category = 7
    elif data == 'Работа':
        category = 8
    elif data == 'Хобби и спорт':
        category = 9
    elif data == 'Недвижимость':
        category = 10
    elif data == 'Транспорт':
        category = 11
    
    user_logo = Users.return_user_logo(post['user_id'])
    related_posts = Posts.category_filter(category)
    len_of_rel_posts = len(related_posts)
    if 'userEmail' in session:
        favPost = favPosts.give_favPostId_of_user(session['userEmail'])
        return render_template('content.html', post = post, menu=menu, title=title, username = session['userName'], uuurl='myprofile', related_posts = related_posts, lang = session['lang'], user_logo = user_logo, favourites = favPost, len_of_rel_posts = len_of_rel_posts, lenOfUserName = len(session['userName']), review = False, cat = dictValues)
    else:
        return render_template('content.html', username = 'Log In', lang = session['lang'], post = post, menu=menu, title=title, uuurl='myprofile', related_posts = related_posts, user_logo = user_logo, len_of_rel_posts = len_of_rel_posts, lenOfUserName = 1, review = False, cat = dictValues)

@app.route('/post_activation/<post_id>/<a_token>/<lang>')
def activation(post_id, a_token, lang):
    try:
        s.loads(a_token, salt='post-activation', max_age=60)
    except (itsdangerous.exc.SignatureExpired, itsdangerous.exc.BadTimeSignature, itsdangerous.exc.BadSignature):
        return render_template('expired_token.html')
    if lang != 'rulang' and lang != 'kzlang':
        lang = 'rulang'
        return redirect(url_for('myposts', lang = 'rulang'))
    post_id = int(post_id)
    Posts.post_activation(post_id)
    return redirect(url_for('myposts', lang = session['lang']))

@app.route('/post_deactivation/<post_id>/<d_token>/<lang>')
def deactivation(post_id, d_token, lang):
    try:
        s.loads(d_token, salt='post-deactivation', max_age=60)
    except (itsdangerous.exc.SignatureExpired, itsdangerous.exc.BadTimeSignature, itsdangerous.exc.BadSignature):
        return render_template('expired_token.html')
    if lang != 'rulang' and lang != 'kzlang':
        lang = 'rulang'
        return redirect(url_for('myposts', lang = 'rulang'))
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
        if lang != 'rulang' and lang != 'kzlang':
            lang = 'rulang'
            return redirect(url_for('payments', lang = 'rulang'))
        session['lang'] = lang
        return render_template('payment.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login'))


@app.route('/review/<post_id>/<lang>', methods = ["POST", 'GET'])
def review(lang, post_id = 0):
    
    if lang != 'rulang' and lang != 'kzlang':
        lang = 'rulang'
    session['lang'] = lang
    if request.method == 'POST':
        
        if post_id == 0:
            user = Users.return_user_to_db(session['userEmail'])
            post_title=request.form['post_title']
            category=request.form['category']
            cost = request.form['post_cost']
            photo = request.files.getlist('post_photo')
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
            for i in photo:
                photo_inf.append(base64.b64encode(i.read()).decode('ascii'))
            if facility == "1":
                facility_inf = 'Цена'
            elif facility == "2":
                facility_inf = 'Возможен обмен'
            elif facility == "3":
                facility_inf = 'Отдам даром'

            post_inf = {'title': post_title, 'username':session['userName'], 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date.strftime("%m/%d/%Y %H:%M"), 'whatsapp_link':whatsapp_link, 'facility':facility_inf, 'photos':photo_inf}
            user_logo = Users.return_user_logo(Users.return_user_id(session['userEmail']))
            return render_template('content.html', post = post_inf, menu=menu, title=title, username = session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), review = True, cat = dictValues, user_logo=user_logo)
        else:
            
            user = Users.return_user_to_db(session['userEmail'])
            post_title=request.form['post_title']
            category=request.form['category']
            cost = request.form['post_cost']
            print('its ok')
            try:
                photo = request.files.getlist('post_photo')
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
            for i in photo:
                photo_inf.append(base64.b64encode(i).decode('ascii'))
            if facility == "1":
                facility_inf = 'Цена'
            elif facility == "2":
                facility_inf = 'Возможен обмен'
            elif facility == "3":
                facility_inf = 'Отдам даром'

            post_inf = {'title': post_title, 'username':session['userName'], 'phone_number':phone_number, 'category':category, "cost":cost, 'description':description, 'post_date':post_date.strftime("%m/%d/%Y %H:%M"), 'whatsapp_link':whatsapp_link, 'facility':facility_inf, 'photos':photo_inf}
            user_logo = Users.return_user_logo(Users.return_user_id(session['userEmail']))
    return render_template('content.html', post = post_inf, menu=menu, title=title, username = session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), review = True, cat = dictValues, user_logo=user_logo)



@app.route('/favorites/<lang>', methods = ['POST', 'GET'])
def favorites(lang):
    Posts.post_deactivation(today = datetime.today())
    if 'userEmail' in session:
        if lang != 'rulang' and lang != 'kzlang':
            lang = 'rulang'
            return redirect(url_for('', lang = 'rulang'))
        session['lang'] = lang
        posts = favPosts.show_favPosts(session['userEmail'])
        print(dictType['1'])
        return render_template('favPosts.html', title = title, menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], cat = dictValues, dictType = dictType, dataCat = dataCat, lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login'))
        

   

@app.route('/authentification', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':  
        if 'email' in request.form:
            user = Users.loginning(email=request.form['email'], password=request.form['psw'])
            if type(user)==NoneType:
                flash("Неправильный логин или пароль! Повторите попытку.")
            elif type(user)==list:
                session['userName']=user[0]
                session['userEmail']=user[1]
                return redirect(url_for('index', lang = session['lang']))
        elif 'newemail' in request.form:
            user = registration(username=request.form['newuname'], email=request.form['newemail'], password=request.form['newpsw'])
            flash(user, 'h')
    return render_template('auth.html', title = title)

@app.route('/logout')
def logout():
    Posts.post_deactivation(today = datetime.today())
    session.pop('userEmail', None)
    session.pop('userName', None)
    return redirect(url_for('index', lang = session['lang'] ))

@app.route('/forgot', methods=['POST','GET'])
def xlogin():
    if request.method=="POST":
        user_email = request.form['uname']
        token = s.dumps(user_email, salt='email-confirm')
        message = f'Это письмо было отправлено для сброса пароля на сайте usharal.kz пользователя с электронным адресом "{user_email}"\nЕсли вы не хотите изменять пароль, не открывайте ссылку и не отправляйте ее никому\n' + url_for('confirm_email', token=token, email=user_email, _external=True)
        send_link(message, user_email)

    return render_template('unableToLog.html', title = title)

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
        new_psw = request.form['newpsw']
        email = request.form['email']
        Users.update_psw(email, new_psw)
        return redirect(url_for('login'))

@app.errorhandler(404)
def error_page(error):
    if 'userName' in session:
        return render_template('error_page.html', menu = menu, lang=session['lang'], lenOfUserName = len(session['userName']))
    else:
        return render_template('error_page.html', menu = menu, lang=session['lang'], lenOfUserName = 1)
# @app.errorhandler(AttributeError)
# @app.errorhandler(KeyError)
# def attributeError_habdler(error):
#     print('ОШИБКА')
#     session.pop('userEmail', None)
#     session.pop('userName', None)
#     return redirect(url_for('index', lang = session['lang'] ))



if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')