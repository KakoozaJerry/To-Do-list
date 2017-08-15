
from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
      app.run(debug=True)