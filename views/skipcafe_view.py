from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, login_manager, login_user, logout_user, login_required
from models import Contact, User

# Blueprintのオブジェクトを生成する
app = Blueprint('views', __name__)

# Web画面
@app.route('/')
def index():
    title = "Skipcafe"
    return render_template('index.html', title=title)

@app.route('/news')
def news():
    title = 'Skipcafe|News'
    subtitle = 'News'
    caption = 'お知らせ一覧'
    return render_template('news.html', title=title, subtitle=subtitle, caption=caption)

@app.route('/news/detail')
def news_datail():
    title = 'Skipcafe|News'
    subtitle = 'News'
    caption = 'お知らせ'
    return render_template('newsdetail.html', title=title, subtitle=subtitle, caption=caption)

@app.route('/access')
def access():
    title = "Skipcafe|Access"
    subtitle = 'Access'
    caption = 'お店案内'
    return render_template('access.html', title=title, subtitle=subtitle, caption=caption)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        form_name = request.form.get('name') # str
        form_url = request.form.get('url') # str
        form_mail = request.form.get('mail') # str
        form_mail_confirmation = request.form.get('mail_confirmation') # str
        form_message = request.form.get('message') # str

        contact = Contact(
            name=form_name,
            url=form_url,
            mail=form_mail,
            mail_confirmation=form_mail_confirmation,
            message=form_message
        )
        db.session.add(contact)
        db.session.commit()
        return redirect(url_for('views.index'))
    else:
        title = "Skipcafe|Contact"
        subtitle = 'Contact'
        caption = 'お問い合わせ'
        return render_template('contact.html', title=title, subtitle=subtitle, caption=caption)


# 管理画面
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        form_user_name = request.form.get('user_name')
        form_email = request.form.get('email')
        form_password = request.form.get('password')
        form_password_confirmation = request.form.get('password_confirmation')
        form_first_name = request.form.get('first_name')
        form_last_name = request.form.get('last_name')

        user = User(
            user_name=form_user_name,
            email=form_email,
            password=generate_password_hash(form_password, method='sha256'),
            password_confirmation=generate_password_hash(form_password_confirmation, method='sha256'),
            first_name=form_first_name,
            last_name=form_last_name
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('views.login'))
    else:
        title = "Skipcafe|SignUp"
        return render_template('signup.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_user_name = request.form.get('user_name')
        form_password = request.form.get('password')

        user = User.query.filter_by(user_name=form_user_name).first()
        if check_password_hash(user.password, form_password):
            login_user(user)
            return redirect('/admin')
    else:
        title = "Skipcafe|Login"
        return render_template('login.html', title=title)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('login')

@app.route('/admin')
def admin():
    title = "Skipcafe管理画面"
    # app_logger.logger.info("TOPページ")
    return render_template('admin.html', title=title)

@app.route('/user/<int:id>/edit/', methods=['GET', 'POST'])
@login_required
def user_edit(user):
    user = User.query.get(user)
    if request.method == "GET":
        title = "Skipcafe管理画面|ユーザ編集"
        return render_template('admin_user_edit.html', user=user, title=title)
    else:
        # 上でインスタンス化したuserのプロパティを更新する
        user.user_name = request.form.get('user_name')
        user.email = request.form.get('email')
        user.password = request.form.get('password')
        user.first_name = request.form.get('first_name')
        user.last_name = request.form.get('last_name')
        # 更新する場合は、add()は不要でcommit()だけでよい
        db.session.commit()
        return redirect('/admin')

@app.route('/user_list', methods=['GET'])
def user_list():
    if request.method == 'GET':
        # DBに登録されたデータをすべて取得する
        title = "Skipcafe管理画面|ユーザ一覧"
        users = User.query.all()
        return render_template('admin_user_list.html', title=title, users=users)