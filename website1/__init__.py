import os
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

migrate = Migrate()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
                            SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
                            SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                            'sqlite:///' + os.path.join(app.instance_path, 'website1.sqlite'),
                            SQLALCHEMY_TRACK_MODIFICATIONS = False
                            )

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # @app.route('/test')
    # def test():
    #     return 'hello, world!'

    @app.route('/code')
    def test():
        return 'Your code is: qwe2p0shfw0'

    from . import welcome
    app.register_blueprint(welcome.bp)

    from . import finish
    app.register_blueprint(finish.bp)

    from . import s1_v2
    app.register_blueprint(s1_v2.bp)

    from . import tutorial
    app.register_blueprint(tutorial.bp)

    from . import OpenQuestions
    app.register_blueprint(OpenQuestions.bp)

    from . import receiveFile
    app.register_blueprint(receiveFile.bp)

    from . import receiveFeedback
    app.register_blueprint(receiveFeedback.bp)

    from website1.GameVersionFolder import game
    app.register_blueprint(game.bp)

    return app
