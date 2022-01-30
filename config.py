class SystemConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/skipcafe?charset=utf8'.format(**{
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
    })

Config = SystemConfig