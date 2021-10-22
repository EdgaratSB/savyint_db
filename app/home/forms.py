from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email, DataRequired

class CreateUser(FlaskForm):
    username = StringField('Username'     , validators=[DataRequired()])
    email    = StringField('Email'        , validators=[DataRequired(), Email()])
    first_name = StringField('First Name' , validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Send')