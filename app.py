from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from flask_mail import Mail,Message


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'replynotallowed23@gmail.com'
app.config['MAIL_PASSWORD'] = 'oxcy sigy lvlq ttyo'
app.config['MAIL_DEFAULT_SENDER'] = 'replynotallowed23@gmail.com'
mail=Mail(app)
app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class Contact(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(25), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     phonenumber = db.Column(db.String(10), nullable=False)
#     description = db.Column(db.Text, nullable=False)

    # def __repr__(self):
    #     return f"Contact('{self.name}', '{self.email}')"

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phoneno = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    desc = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # # Check if the email already exists
        # existing_contact = Contact.query.filter_by(email=form.email.data).first()
        # if existing_contact:
        #     flash('This email is already registered. Please use a different email.', 'danger')
        #     return redirect(url_for('contact'))
        # query = Contact(
        #     name=form.name.data,
        #     email=form.email.data,
        #     phonenumber=form.phoneno.data,
        #     description=form.desc.data
        # )
        # try:
        #     db.session.add(query)
        #     db.session.commit()
            # Send email
            msg = Message('New Contact Form Submission',sender='replynotallowed23@gmail.com',
                          recipients=['piyanshugehani@gmail.com'])
            msg.body = f'''
            New contact form submission:

            Name: {form.name.data}
            Email: {form.email.data}
            Phone Number: {form.phoneno.data}
            Description: {form.desc.data}
            '''
            mail.send(msg)
            print(msg)

            flash('Thanks for contacting us. We will get back to you soon!', 'success')
        # except IntegrityError:
        #     db.session.rollback()
        #     flash('An error occurred. Please try again.', 'danger')
            return redirect(url_for('contact'))
    
    # allobj = Contact.query.all()
    return render_template('contact.html',form=form)

@app.route('/blog')
def handleblog():
    return render_template('handleblog.html')

@app.route('/internshipdetails')
def internshipdetails():
    return render_template('intern.html')

if __name__ == '__main__':
    app.run(debug=True)
