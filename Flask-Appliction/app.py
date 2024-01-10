import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)
# wsgi is usefull when deploying to the web host
wsgi_app = app.wsgi_app

@app.route('/')
def hello():
    '''Render a sample page'''
    now = datetime.now()
    formatted_date = now.strftime("%A, %d, %B, %Y at %X")
    html_content = "<html><head><title>Hello Flask</title></head><body>"
    html_content += "<strong>Hello Flask!</strong> on " + formatted_date
    html_content += "</body></html>"
    return html_content


if __name__ == "__main__":
    HOST = os.environ.get("SERVER_HOST", "localhost")
    try:
        PORT = int(os.environ.get("SERVER_PORT", '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)