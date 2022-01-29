from flask import Blueprint, render_template
# from models.contact import Contact

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

@app.route('/contact')
def contact():
    title = "Skipcafe|Contact"
    subtitle = 'Contact'
    caption = 'お問い合わせ'
    return render_template('contact.html', title=title, subtitle=subtitle, caption=caption)