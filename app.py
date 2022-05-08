from flask_bootstrap import Bootstrap
from flask import (
    Flask,
    render_template,
    redirect
)


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return redirect('/home')


@app.route('/home/')
def home():
    return render_template('index.html', title='Home')


@app.route('/about-me/')
def about():
    return render_template('about-me.html', title='About Me')


@app.route('/interests/')
def interests():
    return render_template('interests.html', title='Home')


@app.route('/projects/')
def projects():
    return render_template('coming-soon.html', title='Projects')


if __name__ == '__main__':
    app.run(debug=True)
