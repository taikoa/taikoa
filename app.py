from flask import Flask, render_template, request
from flaskext.babel import Babel
app = Flask(__name__)
#app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['es', 'fr', 'en'])


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/labs")
def labs():
    return render_template('labs.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
