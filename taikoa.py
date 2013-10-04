import re

from flask import Flask, render_template, request, flash, redirect
from flaskext.babel import Babel
from flask.ext.mail import Mail, Message
from flask.ext.cache import Cache
from flask.ext.assets import Environment
from raven.contrib.flask import Sentry


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
babel = Babel(app)
cache = Cache(app)
mail = Mail(app)
assets = Environment(app)
sentry = Sentry(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['es', 'fr', 'en'])


@cache.cached(timeout=50)
@app.route("/")
def index():
    return render_template('index.html', active='home')


@cache.cached(timeout=50)
@app.route("/projects")
def projects():
    return render_template('projects.html', active='project')


@cache.cached(timeout=50)
@app.route("/about")
def about():
    return render_template('about.html', active='about')


@cache.cached(timeout=50)
@app.route("/about/me")
def about_me():
    return render_template('about-me.html', active='about')


@cache.cached(timeout=50)
@app.route("/contact")
def contact():
    return render_template('contact.html', active='contact')


@app.route("/contact_form", methods=['POST'])
def contact_form():
    email_re = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
    r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)

    company = request.form['company']
    subject = request.form['subject']
    content = request.form['message']
    client_email = request.form['email']

    if not email_re.match(client_email):
        flash('Form error, please fix the error in the email')
        return render_template('contact.html')

    msg = Message('-'.join([company, subject]),
                  sender=client_email,
                  recipients=[app.config['EMAIL']])
    msg.body = content
    mail.send(msg)
    flash('Message sent correctly, Thank you.')
    return redirect('/')


if __name__ == "__main__":
    app.run()
