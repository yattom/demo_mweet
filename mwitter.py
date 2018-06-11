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


class Tweet:
    tweets = []

    @staticmethod
    def 新規作成(user, text):
        tweet = Tweet()
        tweet.author = user
        tweet.text = text
        Tweet.tweets.append(tweet)
        print(Tweet.tweets)
        return tweet

    @staticmethod
    def 取得(author):
        return [t for t in Tweet.tweets if t.author == author]


User.新規作成('自分')


@app.route("/")
def index():
    users = User.users
    tweets = Tweet.tweets
    return render_template('index.html', users=users, tweets=tweets)

@app.route("/login")
def login():
    session['username'] = request.args.get('login')
    return redirect('timeline')

@app.route("/timeline")
def users_timeline():
    user=User.取得(session['username'])
    tweets = Tweet.tweets
    return render_template('timeline.html', user=user, tweets=tweets)

@app.route("/users/create", methods=['POST'])
def create_user():
    User.新規作成(request.form['name'])
    return redirect('/')

@app.route("/users/<name>/tweets/create", methods=['POST'])
def create_tweet(name):
    user = User.取得(name)
    tweet = Tweet.新規作成(user=user, text=request.form['text'])
    return redirect(url_for('users_timeline', name=user.name))

@app.route("/users/<name>")
def user(name):
    user=User.取得(name)
    tweets = Tweet.取得(author=user)
    return render_template('user.html', user=user, tweets=tweets)

@app.route("/users/<name>/followings", methods=['POST'])
def follow_user(name):
    user = User.取得(name)
    tweet = Tweet.新規作成(user=user, text=request.form['text'])
    return redirect(url_for('users_timeline', name=user.name))

