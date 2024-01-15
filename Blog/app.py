from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [{
    "author": 'Lewis Njaci',
    " title": "Blog post",
    "content": 'Blog'
},
    {
        "None",
    }
]

@app.route('/')
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)