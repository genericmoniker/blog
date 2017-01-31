from flask import Flask


app = Flask(__name__)


@app.route('/search')
def search():
    return 'No matches found'


if __name__ == '__main__':
    app.run()
