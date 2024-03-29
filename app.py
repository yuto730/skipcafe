import os
from flask import Flask
from views import skipcafe_view
from database import db, login_manager
import models
import config

def create_app():
    app = Flask(__name__)

    # DB設定の読み込み
    app.config.from_object('config.Config')
    app.config['SECRET_KEY'] = os.urandom(24)
    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(skipcafe_view.app)
    return app

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)