from flask import Flask, render_template, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
from datetime import datetime

app = Flask(__name__)
app.secret_key = "random secret"

# SQL Alchemy
app.config['SECRET_KEY'] = 'fdfd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Database instance
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    
    def __repr__(self):
        return f"User('{self.username}')"

#oauth config
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='505058630686-q599kb0qd33eqt26pdk5m9o0narocdus.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://acounts.google.com/o/oauth2/token',
    acess_token_params=None,
    authorize_url='https://acounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/ouath2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)

# Main Page
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/login')
def login():
    google = oauth.creat_client('google')
    redirect_url = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_url)

@aap.route('/logout')
def logout():
    pass

@app.route('/callback')
def callback():
    pass

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    userinfo = resp.json()
    # do something with the token and profile
    return redirect('/')


@app.route('/inside')
def inside():
    pass


