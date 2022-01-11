# This file contains the application factory.
# also, tells Python to treat this file as a package.
import os

from flask import Flask

# Application Factory function
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True) # creates the Flask instance
    app.config.from_mapping(
        SECRET_KEY = 'dev', #encrypt session data
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensuring the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import blueprints
    from .views import views
    from .auth import auth

    # register with app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
