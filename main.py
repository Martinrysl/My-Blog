import requests
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    data = requests.get('https://api.npoint.io/e0358cf251691096282d').json()
    return render_template('index.html', data=data)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/post/<int:index>")
def post(index):
    data = requests.get('https://api.npoint.io/e0358cf251691096282d').json()
    requested_post = None
    for data_post in data:
        if data_post["id"] == index:
            requested_post = data_post
    return render_template('post.html', data=requested_post)


if __name__ == '__main__':
    app.run(debug=True)

