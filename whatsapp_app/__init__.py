from flask import Flask

from whatsapp_app.config import Config
from whatsapp_app.models import db
from whatsapp_app.auth import auth_bp
from whatsapp_app.dashboard import dashboard_bp
from whatsapp_app.webhook import webhook_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(webhook_bp)

    with app.app_context():
        db.create_all()

    return app
