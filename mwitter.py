# cofing: utf-8

from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "THISISNOTASECRET"

class User:
    users = []

    @staticmethod
    def 新規作成(name):
        user = User()
        user.name = name
        User.users.append(user)
        return user

    @staticmethod
    def 取得(name):
        return [u for u in User.users if u.name == name][0]

    def ツイートする(self, text):
        tweet = Tweet.新規作成(self, text)
        return tweet

    def 自分のツイート(self):
        return Tweet.tweet_from_user(self)

class Tweet:
    tweets = []

    @staticmethod
    def 新規作成(author, text):
        tweet = Tweet()
        tweet.author = author
        tweet.text = text
        Tweet.tweets.append(tweet)
        return tweet

    @staticmethod
    def tweet_from_user(author):
        return [t for t in Tweet.tweets if t.author == author]


class Follow:
    follows = []

User.新規作成('自分')


@app.route("/")
def index():
    users = User.users
    tweets = []
    return render_template('index.html', users=users, tweets=tweets)

@app.route("/login")
def login():
    session['login'] = request.args.get('login')
    return redirect('timeline')

@app.route("/timeline")
def users_timeline():
    user = User.取得(session['login'])
    tweets = user.自分のツイート()
    return render_template('timeline.html', user=user, tweets=tweets)

@app.route("/users/create", methods=['POST'])
def create_user():
    return redirect('/')

@app.route("/users/<name>/tweets/create", methods=['POST'])
def create_tweet(name):
    user = User.取得(name)
    tweet = user.ツイートする(request.form['text'])
    return redirect(url_for('users_timeline', name=user.name))

@app.route("/users/<name>")
def user(name):
    user = None
    tweets = []
    return render_template('user.html', user=user, tweets=tweets)

@app.route("/users/<name>/follow", methods=['POST'])
def follow_user(name):
    return redirect(url_for('user', name=target.name))

