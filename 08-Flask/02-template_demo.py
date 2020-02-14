from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def index():
    url = 'http://baidu.com/'
    return render_template('index.html', url_string=url)


if __name__ == '__main__':
    app.run(debug=True)