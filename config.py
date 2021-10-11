
class Config(object):
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail Configuration
    MAIL_SERVER = 'smtp.gmail.com'


class Debug(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    DEBUG = True

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:password@localhost/daniel'
    DEBUG = False


config_dict = {'Debug': Debug, 'Production': Production}