from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get_pdf')
def pdf():
    pass


@app.route('/get_web')
def web():
    pass


@app.route('/get_document')
def document():
    pass


if __name__ == '__main__':
    app.run()
