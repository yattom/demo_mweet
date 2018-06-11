# cofing: utf-8

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "THISISNOTASECRET"

class User:
    users = []

    @staticmethod
    def 新規作成(name):
        pass

class Tweet:
    tweets = []

class Follow:
    follows = []

User.新規作成('自分')


@app.route("/")
def index():
    users = []
    tweets = []
    return render_template('index.html', users=users, tweets=tweets)

@app.route("/login")
def login():
    session['login'] = request.args.get('login')
    return redirect('timeline')

@app.route("/timeline")
def users_timeline():
    user = None
    tweets = []
    return render_template('timeline.html', user=user, tweets=tweets)

@app.route("/users/create", methods=['POST'])
def create_user():
    return redirect('/')

@app.route("/users/<name>/tweets/create", methods=['POST'])
def create_tweet(name):
    return redirect(url_for('users_timeline', name=user.name))

@app.route("/users/<name>")
def user(name):
    user = None
    tweets = []
    return render_template('user.html', user=user, tweets=tweets)

@app.route("/users/<name>/follow", methods=['POST'])
def follow_user(name):
    return redirect(url_for('user', name=target.name))

