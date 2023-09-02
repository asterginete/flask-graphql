from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_caching import Cache
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_babel import Babel
from flask_oauthlib.client import OAuth
from flask_principal import Principal

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()
jwt = JWTManager()
limiter = Limiter()
cache = Cache()
migrate = Migrate()
socketio = SocketIO()
babel = Babel()
oauth = OAuth()
principal = Principal()

def create_app(config_name="default"):
    app = Flask(__name__)

    # Load configurations
    # For the sake of this example, we'll use a simple configuration method
    # In a real-world scenario, you'd likely load configurations from a separate file or environment variables
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database-file.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    babel.init_app(app)
    oauth.init_app(app)
    principal.init_app(app)

    # Register blueprints, error handlers, etc.
    # For example:
    # from .views import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app
