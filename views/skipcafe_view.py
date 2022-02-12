from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from models import Contact

# Blueprintのオブジェクトを生成する
app = Blueprint('views', __name__)

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
    if request.method == 'GET':
        title = "Skipcafe|Contact"
        subtitle = 'Contact'
        caption = 'お問い合わせ'
        return render_template('contact.html', title=title, subtitle=subtitle, caption=caption)

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
