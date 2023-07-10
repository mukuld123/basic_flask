from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import *

app = Flask(__name__)

app.config['SECRET_KEY'] = '8c1370dfb8d4967de99dbfb8031fc05c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/code')
def code():
    return render_template('code.html')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate():
        # print('validated')
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate():
        # print('validated')
        return redirect(url_for('home'))
    return render_template('login.html', form = form)


if __name__ == '__main__':
    app.run(debug = True)