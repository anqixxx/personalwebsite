from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message
from forms import ContactForm
import pandas as pd
from datetime import datetime, timezone
from csv import writer, DictWriter



app = Flask(__name__)

# routing some funtion to our home function, which turns hello world
@app.route('/')
def home():
    return render_template('default.html')

# specifiying the path, the actual route the server should go to, 
# and what is will return at that specific point
@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/technicalexperience')
def technicalexperience():
    return render_template('technicalexperience.html')

@app.route('/technicalprojects')
def technicalprojects():
    return render_template('technicalprojects.html')

# @app.route('/nontechnicalexperience')
# def nontechnicalexperience():
#     return render_template('nontechnicalexperience.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # form = ContactForm()
    # if request.method == 'POST':
    #     result = request.form
    #     email = request.form["username"]
    #     message = request.form["query"]
    #     time = datetime.now()
    #     res = pd.DataFrame({'email': email, 'message': message, 'time': time}, index=[0])
    #     res.to_csv('./contactusMessage.csv', mode='a', index=False, header=False)

    #     # field_names = List=['Email','Message','Time']
    #     # # Dictionary
    #     # dict={{'Email': email, 'Message': message}, 'Time'= datetime.now()}
       
    #     # # Open your CSV file in append mode
    #     # # Create a file object for this file
    #     # with open('event.csv', 'a') as f_object:
        
    #     # # Pass the file object and a list 
    #     # # of column names to DictWriter()
    #     # # You will get a object of DictWriter
    #     # dictwriter_object = DictWriter(f_object, fieldnames=field_names)
  
    #     # #Pass the dictionary as an argument to the Writerow()
    #     # dictwriter_object.writerow(dict)
  
    #     # #Close the file object
    #     # f_object.close()
        
    #     return render_template('user.html', result=result)
    # else:
    #     return render_template('contact.html', form=form)
    return render_template('contact.html')


# want to render html content 
if __name__ == '__main__':
    app.run()

