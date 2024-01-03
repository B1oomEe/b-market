import re
from flask_wtf import FlaskForm
from pydantic.config import ConfigDict
from wtforms import StringField, SubmitField, PasswordField, BooleanField, EmailField, SelectField, TextAreaField, FileField
from wtforms.validators import InputRequired, Email, Length, EqualTo, DataRequired
from flask_login import UserMixin

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[
		InputRequired(), 
		# Length(min=2, max=32, message="Username must be at least 2 characters long and no more than 32")
	])
	email = EmailField('Email', validators=[
		InputRequired(), 
		# Email()
	])
	contact_email = EmailField('Contact email', validators=[
		InputRequired(), 
		# Email()
	])
	password = PasswordField('Password', validators=[
		InputRequired(), 
		# Length(min=6, max=32, message="Password must be at least 6 characters long and no more than 32")
	])
	confirm_password = PasswordField('Confirm password', validators=[
		InputRequired(),
	])
	rememberMe = BooleanField('Remember Me')
	submit = SubmitField('Register')


class RegistrationFormValidator():
	def __init__(self, username: str, email: str, contact_email: str, password: str, confirm_password: str):
		self.username = username
		self.email = email
		self.contact_email = contact_email
		self.password = password
		self.confirm_password = confirm_password
		self.email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

	def validateEmail(self) -> tuple:
		if not self.email_pattern.match(self.email):
			return False, "Incorrect email"
		return True, "Successful email validate"
	
	def validateContactEmail(self) -> tuple:
		if not self.email_pattern.match(self.email):
			return False, "Incorrect contact email"
		return True, "Successful contact email validate"
	
	def validateUsername(self) -> tuple:
		if len(self.username) < 2 or len(self.username) > 32 or any(char.isalpha() for char in self.password):
			return False, "Incorrect username"
		return True, "Successful username validate"

	def validatePassword(self) -> tuple:
		if len(self.password) < 8 or len(self.password) > 32:
			return False, "Password must be at least from 8 to 32 characters long"
		if not any(char.isdigit() for char in self.password) or not any(char.isalpha() for char in self.password):
			return False, "Password must contain at least one digit or letter"
		return True, "Successful password validate"

	def validatePasswordConfirm(self) -> tuple:
		if self.password != self.confirm_password:
			return False, "Passwords does't match"
		return True, "Successful password matching validate"


	def validateForm(self):
		emailValidity = self.validateEmail()
		if not emailValidity:
			return emailValidity
		
		contactEmalValidity = self.validateContactEmail()
		if not contactEmalValidity:
			return contactEmalValidity
		
		passwordValidity = self.validatePassword()
		if not passwordValidity:
			return passwordValidity
		
		passwordConfirmValidity = self.validatePasswordConfirm()
		if not passwordConfirmValidity:
			return passwordConfirmValidity
		
		return True, "Successful registration"
