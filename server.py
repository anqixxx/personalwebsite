from flask import Flask, render_template, redirect, request
# from flask_mail import Mail
from forms import ContactForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'penguin'
# mail = Mail(app)


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
        # email == request.form['username'].replace('','').lower()
        result = request.form
        return render_template('user.html', result=result)
        # result is immutable dictionary, key value pairs
    return render_template('contact.html', form=form)

# want to render html content 
if __name__ == '__main__':
    app.run()

