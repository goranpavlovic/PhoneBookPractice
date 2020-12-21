from flask import Flask


class Config:
    pass


def create_app():
    app: Flask = Flask(__name__)
    app.config.from_object(Config)

    from server.views import spectree
    from server.views.infrastructure import infra_blueprint

    spectree.register(app)

    app.register_blueprint(infra_blueprint)

    return app

app = create_app()
