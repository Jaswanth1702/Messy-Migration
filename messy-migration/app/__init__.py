from flask import Flask
from config import Config
from app.extensions import db  # ✅
from app.utils.error_handlers import register_error_handlers  # ✅
from app.routes.user_routes import user_bp  # ✅


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(user_bp, url_prefix='/')

    register_error_handlers(app)

    @app.route('/')
    def health_check():
        return {'status': 'success', 'message': 'API is up and running'}

    return app

