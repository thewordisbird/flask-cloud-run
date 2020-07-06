from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, HiddenField, DateField, FileField, PasswordField
from wtforms.validators import DataRequired, ValidationError, optional, Email, EqualTo  

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])

class InputForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone')
    email = StringField('Email', validators=[])