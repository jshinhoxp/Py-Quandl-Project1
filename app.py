from flaskr import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# Main Page
@app.route('/')
def index():
    return render_template('home.html')


