from flask import Flask
from views import skipcafe_view
from database import init_db
import config

def create_app():
    app = Flask(__name__)

    # DB設定の読み込み
    app.config.from_object('config.Config')
    init_db(app)

    app.register_blueprint(skipcafe_view.app)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
