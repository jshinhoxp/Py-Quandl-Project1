from flask import Flask

def create_app():
    app = Flask(__name___
    app.config['SECRET_KEY'] = 'dfjkdl;afdslaj' #encrypt session data
    
    return app
