from flask import Flask, render_template, request, flash
from flaskext.babel import Babel
from flask.ext.mail import Mail, Message

app = Flask(__name__)
#app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)
mail = Mail(app)


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


@app.route("/contact_form", methods=['POST'])
def contact_form():
    # FIXME Validation
    company = request.form['company']
    subject = request.form['subject']
    content = request.form['message']
    client_email = request.form['email']
    msg = Message('-'.join([company, subject]),
                  sender=client_email,
                  recipients=["javi@javaguirre.net"])
    msg.body = content
    mail.send(msg)
    flash('Message sent correctly, Thank you.')

    return render_template('contact.html')

if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'Z0Zr98j/3yX R~XHH!jmN]LWX/,?RAA'
    app.run()
