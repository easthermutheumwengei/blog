from flask import Flask
# from config import config_options
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_mail import Mail
from config import DevConfig, ProdConfig

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()
mail = Mail()


def create_app(config_name):

    app = Flask(__name__)
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    app.config.update(dict(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USE_SSL=False,
        MAIL_USERNAME='essyhaddasah6@gmail.com',
        MAIL_PASSWORD='essy1234',
    ))


    simple.init_app(app)
    mail.init_app(app)

    app.config.from_object(DevConfig)
    # app.config.from_object(ProdConfig)

    app.config['TEMPLATES_AUTO_RELOAD'] = True




    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Will add the views and forms
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

