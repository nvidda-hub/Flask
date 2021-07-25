from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_user_name(self, username_to_check):
        # checking into database for username
        user = User.query.filter_by(user_name=username_to_check.data).first()
        if user:    # if user exists then this means user already in database otherwise it's null
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
            email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
            if email_address:
                raise ValidationError('Email already exists! Please try a different username')

    user_name = StringField(label='User Name : ', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address : ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password : ', validators=[Length(min=6, max=30), DataRequired()])        # password
    password2 = PasswordField(label='Confirm Password : ')        # for confirm password validators=[EqualTo(password1), DataRequired()]
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    user_name = StringField(callable('User Name: '), validators=[DataRequired()])
    password = PasswordField(callable('Password: '), validators=[DataRequired()])
    submit = SubmitField(label='Sign In')