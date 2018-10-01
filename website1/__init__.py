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

    from . import receiveFeedback
    app.register_blueprint(receiveFeedback.bp)

    from . import finish
    app.register_blueprint(finish.bp)

    from . import OpenQuestions
    app.register_blueprint(OpenQuestions.bp)

######## Poster Version ###########
    from website1.PosterVersionPy import welcome
    app.register_blueprint(welcome.bp)

    from website1.PosterVersionPy import s1_v2
    app.register_blueprint(s1_v2.bp)

    from website1.PosterVersionPy import tutorial
    app.register_blueprint(tutorial.bp)

    from website1.PosterVersionPy import receiveFile
    app.register_blueprint(receiveFile.bp)

    from website1.PosterVersionPy import follow_up
    app.register_blueprint(follow_up.bp)

########## Game Version ############
    from website1.GameVersionPy import game
    app.register_blueprint(game.bp)

    from website1.GameVersionPy import gameIntro
    app.register_blueprint(gameIntro.bp)

    from website1.GameVersionPy import receiveFile_ver_game
    app.register_blueprint(receiveFile_ver_game.bp)

########## Easy Version ############
    from website1.EasyVersionPy import EasyContent
    app.register_blueprint(EasyContent.bp)

    from website1.EasyVersionPy import EasyIntro
    app.register_blueprint(EasyIntro.bp)

    from website1.EasyVersionPy import receiveFile_ver_Easy
    app.register_blueprint(receiveFile_ver_Easy.bp)

    return app
