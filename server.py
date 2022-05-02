from flask import Flask, render_template, redirect, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'penguin'

# routing some funtion to our home function, which turns hello world
@app.route('/')
def home():
    return 'This is My Website'

# specifiying the path, the actual route the server should go to, 
# and what is will return at that specific point
@app.route('/about')
def about():
    return 'The About Page'

@app.route('/resume')
def resume():
    return 'The Resume Page'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
        # result is immutable dictionary, key value pairs
    return render_template('signup.html', form=form)

# want to render html content 
if __name__ == '__main__':
    app.run()

