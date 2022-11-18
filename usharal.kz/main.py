from types import NoneType
from flask import Flask, render_template, url_for, request, redirect, flash, session
from itsdangerous import URLSafeTimedSerializer
import itsdangerous
from send_email import send_link
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from db import Users, registration, Posts, Photos, favPosts

app = Flask(__name__)
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

def add_favPost(user_id, post_id):
    post = favPosts(user_id, post_id)

@app.route('/')
def index():

    Posts.post_deactivation(today = datetime.today())
    posts = Posts.show_all_posts()
    if 'userEmail' in session:
        return render_template('index.html',title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', posts = posts)
    else:
        return render_template('index.html',title = 'usharal.kz', menu = menu, username=f'Log In', uuurl='authentification', posts = posts)

@app.route('/messages')
def messages():
    if 'userEmail' in session:
        return render_template('messageSection.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile')
    else:
        return redirect(url_for('login'))

@app.route('/myprofile', methods=['POST', 'GET'])
def myprofile():
    if 'userEmail' in session:
        if request.method == 'POST':
            username = request.form['username']
            logo = request.files['logo'].read()
            phone_number = request.form['phone_number']
            password = request.form['password']
            Users.edit_user_information(session['userEmail'], logo, phone_number, password, username)
        
        user_information = Users.show_user_information(session['userEmail'])
        return render_template('myProfile.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', user = user_information)
    else:
        return redirect(url_for('login'))

@app.route('/mypost')
def myposts():
    Posts.post_deactivation(today = datetime.today())
    if 'userEmail' in session:
        posts = Posts.show_posts_of_user(session['userEmail'])
        return render_template('myPosts.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', posts = posts)
    else:  
        return redirect(url_for('login'))

def phone_numbers_to_waLink(number):
    res = ''
    for i in number:
        if i in '1234567890':
            res+=i
    return res

@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    if 'userName' in session:
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
            for i in range(len(photo)):
                photos = Photos(photo[i].read(), post)
        return render_template('newPost.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile')
    else:
        return redirect(url_for('login'))

@app.route('/content/<post_id>')
def content(post_id):
    Posts.post_deactivation(today = datetime.today())
    if 'userEmail' in session:
        related_posts = []
        post = Posts.show_one_post(post_id)
        return render_template('content.html', post = post, menu=menu, title='usharal.kz', username = session['userName'], uuurl='myprofile', related_posts = related_posts)
    else:
        post = Posts.show_one_post(post_id)
        return render_template('content.html', post = post, menu=menu, username = 'Log In')

@app.route('/post_activation/<post_id>')
def activation(post_id):
    post_id = int(post_id)
    Posts.post_activation(post_id)
    return redirect(url_for('myposts'))

@app.route('/post_deactivation/<post_id>')
def deactivation(post_id):
    post_id = int(post_id)
    Posts.post_deactivation_by_user(post_id)
    return redirect(url_for('myposts'))

@app.route('/vippurchase/<post_id>')
def vippurchase(post_id):
    post_id = int(post_id)
    Posts.post_to_vip(post_id)
    return redirect(url_for('index'))

@app.route('/payments')
def payments():
    if 'userEmail' in session:
        return render_template('payment.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile')
    else:
        return redirect(url_for('login'))

@app.route('/favorites')
def favorites():
    Posts.post_deactivation(today = datetime.today())
    if 'userEmail' in session:
        posts = favPosts.show_favPosts(session['userEmail'])
        return render_template('favPosts.html', title = 'usharal.kz', menu = menu, username=session['userName'], uuurl='myprofile', posts = posts)
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
                return redirect(url_for('index'))
        elif 'newemail' in request.form:
            user = registration(username=request.form['newuname'], email=request.form['newemail'], password=request.form['newpsw'])
            flash(user)
    return render_template('auth.html', title = 'usharal.kz')

@app.route('/logout')
def logout():
    Posts.post_deactivation(today = datetime.today())
    session.pop('userEmail', None)
    session.pop('userName', None)
    return redirect(url_for('index'))

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
    return render_template('error_page.html', menu = menu)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')