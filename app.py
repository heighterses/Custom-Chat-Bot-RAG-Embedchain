from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_text')
def text():
    return render_template('Text.html')


@app.route('/get_web')
def web():
    return render_template('Web.html')


@app.route('/get_document')
def document():
    return render_template('Document.html')


@app.route('/qa')
def qa():
    return render_template('QnA.html')


if __name__ == '__main__':
    app.run()
