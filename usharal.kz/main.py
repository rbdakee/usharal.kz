import base64
from types import NoneType
from flask import Flask, render_template, url_for, request, redirect, flash, session
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
        print(category)
        if 'userEmail' in session:
            favPost = favPosts.give_favPostId_of_user(session['userEmail'])
            return render_template('index.html',title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], favourites = favPost, category = data, cat = dictValues, lenOfUserName = len(session['userName']))

        else:
            return render_template('index.html',title = 'usharal.kz', menu = menu, username=f'Log In', uuurl='authentification', posts = posts, lang = session['lang'], category = data, cat = dictValues, lenOfUserName = 1)
    if 'userEmail' in session:
        posts = Posts.show_all_posts()
        favPost = favPosts.give_favPostId_of_user(session['userEmail'])
        return render_template('index.html',title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], favourites = favPost, category = 'Все категории', cat = dictValues, lenOfUserName = len(session['userName']))

    else:
        posts = Posts.show_all_posts()
        return render_template('index.html',title = 'usharal.kz', menu = menu, username=f'Log In', uuurl='authentification', posts = posts, lang = session['lang'], category = 'Все категории', cat = dictValues, lenOfUserName = 1)
    

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
        return render_template('messageSection.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login'))

@app.route('/myprofile/<lang>', methods=['POST', 'GET'])
def myprofile(lang='rulang'):
    if 'userEmail' in session:
        if request.method == 'POST':
            username = request.form['username']
            session['userName'] = username
            logo = request.files['logo'].read()
            phone_number = request.form['phone_number']
            password = request.form['password']
            # prevpass = request.form['userPrevPassword']
            Users.edit_user_information(session['userEmail'], logo, phone_number, password, username)
        session['lang'] = lang
        user_information = Users.show_user_information(session['userEmail'])
        return render_template('myProfile.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', user = user_information, lang=session['lang'], lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login'))

@app.route('/mypost/<lang>')
def myposts(lang):
    Posts.post_deactivation(today = datetime.today())
    if 'userEmail' in session:
        session['lang'] = lang
        if lang != 'rulang' and lang != 'kzlang':
            lang = 'rulang'
            return redirect(url_for('myposts', lang = 'rulang'))
        posts = Posts.show_posts_of_user(session['userEmail'])
        return render_template('myPosts.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], cat = dictValues, lenOfUserName = len(session['userName']))
    else:  
        return redirect(url_for('login'))

def phone_numbers_to_waLink(number):
    res = ''
    for i in number:
        if i in '1234567890':
            res+=i
    return res

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
            description = request.form['post_description']
            phone_number = request.form['phone_number']
            whatsapp_phone_number = request.form['whatsapp_phone_number']
            whatsapp_link = f'https://wa.me/{phone_numbers_to_waLink(whatsapp_phone_number)}'
            deactivate_date = datetime.today() + timedelta(days=14)
            status = True
            advertisement = False
            facility = request.form['radio']
            post_date = datetime.today()
            post = Posts(user, post_title, phone_number, category, cost, description, post_date, deactivate_date, whatsapp_link, status, advertisement, facility)
            for i in photo:
                photos = Photos(i.read(), post)
            
        return render_template('newPost.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login'))

@app.route('/edit_post/<post_id>', methods = ['POST', 'GET'])
def edit_post(post_id):
    post = Posts.show_one_post(post_id)

    if request.method == 'POST':
        id = post_id
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
        post = Posts(id, user, post_title, phone_number, category, cost, description, post_date, deactivate_date, whatsapp_link, status, advertisement, facility)
        for i in range(len(photo)):
            photos = Photos(photo[i].read(), post)
        

    post['whatsapp_link'] = post['whatsapp_link'].split('/')[-1]
    return render_template('editPost.html', post = post, menu = menu, username=session['userName'], uuurl='myprofile', lenOfUserName = len(session['userName']))

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
    if 'userEmail' in session:
        post = Posts.show_one_post(post_id)
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
        favPost = favPosts.give_favPostId_of_user(session['userEmail'])
        return render_template('content.html', post = post, menu=menu, title='usharal.kz', username = session['userName'], uuurl='myprofile', related_posts = related_posts, lang = session['lang'], user_logo = user_logo, favourites = favPost, len_of_rel_posts = len_of_rel_posts, lenOfUserName = len(session['userName']), review = False, cat = dictValues)
    else:
        post = Posts.show_one_post(post_id)
        return render_template('content.html', post = post, menu=menu, username = 'Log In', lang = session['lang'], review = False)

@app.route('/post_activation/<post_id>')
def activation(post_id):
    post_id = int(post_id)
    Posts.post_activation(post_id)
    return redirect(url_for('myposts'))

@app.route('/post_deactivation/<post_id>/<lang>')
def deactivation(post_id, lang):
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
        return render_template('payment.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']))
    else:
        return redirect(url_for('login'))


@app.route('/review/<lang>', methods = ["POST", 'GET'])
def review(lang, post_inf = {}):
    if lang != 'rulang' and lang != 'kzlang':
        lang = 'rulang'
    session['lang'] = lang
    if request.method == 'POST':
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
        return render_template('content.html', post = post_inf, menu=menu, title='usharal.kz', username = session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), review = True, cat = dictValues, user_logo=user_logo)
    return render_template('content.html', post = post_inf, menu=menu, title='usharal.kz', username = session['userName'], uuurl='myprofile', lang = session['lang'], lenOfUserName = len(session['userName']), review = True, cat = dictValues, user_logo=user_logo)



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
        return render_template('favPosts.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', posts = posts, lang = session['lang'], cat = dictValues, dictType = dictType, dataCat = dataCat, lenOfUserName = len(session['userName']))
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
            flash(user)
    return render_template('auth.html', title = 'usharal.kz')

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

    return render_template('unableToLog.html', title = 'usharal.kz')

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
   
    return render_template('error_page.html', menu = menu, lang=session['lang'], lenofUserName = len(session['userName']))




if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')