import os
from flask import Flask

app = Flask(__name__)
# wsgi is usefull when deploying to the web host
wsgi_app = app.wsgi_app

@app.route('/')
def hello():
    '''Render a sample page'''
    return "<h1>Hello World!!!</h1>"


if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)