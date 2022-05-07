from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message
from forms import ContactForm
import os

app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'anqiwebsitetest@gmail.com',
    "MAIL_PASSWORD": 'websitetester1'
    # "MAIL_USERNAME": os.environ['EMAIL_USER'],
    # "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
}

app.config['SECRET_KEY'] = 'penguin'
app.config.update(mail_settings)
mail = Mail(app)

# if __name__ == '__main__':
#     with app.app_context():
#         msg = Message(subject="Hello",
#                       sender=app.config.get("MAIL_USERNAME"),
#                       recipients=["anqix2002@gmail.com"], # replace with your email for testing
#                       body="This is a test email I sent with Gmail and Python!")
#         mail.send(msg)


def sendContactForm(result):
    msg = Message(subject="Contact Form from Website", 
            sender=app.config.get("MAIL_USERNAME"), 
            recipients="anqix2002@gmail.com") 

    msg.body = """
        Hey Anqi,

        You just recieved a contact form!

        Email: {}
        Message: {}
    """.format(result['email'], result['message'])

    mail.send(msg)

# routing some funtion to our home function, which turns hello world
@app.route('/')
def home():
    return render_template('default.html')

# specifiying the path, the actual route the server should go to, 
# and what is will return at that specific point
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/technicalexperience')
def technicalexperience():
    return render_template('technicalexperience.html')

@app.route('/technicalprojects')
def technicalprojects():
    return render_template('technicalprojects.html')

@app.route('/nontechnicalexperience')
def nontechnicalexperience():
    return render_template('nontechnicalexperience.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.is_submitted():

        result = request.form
        # result['email'] = request.form['username']
        # result['message'] = request.form['message'] 

        # sendContactForm(result)

        return render_template('user.html', result=result)

        # result is immutable dictionary, key value pairs
    return render_template('contact.html', form=form)

# want to render html content 
if __name__ == '__main__':
    app.run()

