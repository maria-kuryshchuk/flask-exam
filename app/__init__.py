from flask import Flask

from .api_rest import rest

# Local Modules
from .extensions import db, ma
from .swagger import swagger_bp

# Blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

        app.register_blueprint(swagger_bp, url_prefix="/swagger")
        app.register_blueprint(rest.api_rest_bp, url_prefix="/api")

    # print("\n<<=== URL MAP ===>>")
    # print(app.url_map)
    # print()
    return app
