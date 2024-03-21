from flask import Flask

app = Flask (__name__)


@app.route('/')
def hello():
    return ' \n \n \n \t \t \t \t Welcome to kaustubh World, let connect on linkdin for better collaboration to learn Docker!'
if __name__ == '__main__':
    app.run (debug=True, host='0.0.0.0')