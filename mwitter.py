# cofing: utf-8

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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


User.新規作成('自分')


@app.route("/")
def index():
    return render_template('index.html', users=User.users, tweets=[])


@app.route("/users/<name>/timeline")
def users_timeline(name):
    return render_template('index.html', user=User.取得(name), users=[], tweets=[])

@app.route("/users/create", methods=['POST'])
def create_user():
    User.新規作成(request.form['name'])
    return redirect('/')
