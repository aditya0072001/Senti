from flask import Flask,redirect,url_for,render_template
app = Flask(__name__)

#target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)
@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/<name>')
def hello_name(name):
    return render_template("index.html",content=name)

if __name__ == '__main__':
    app.run()