import re
from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, BooleanField, EmailField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
	email = EmailField('Email', validators=[
		InputRequired(), 
		# Email()
	])
	password = PasswordField('Password', validators=[
		InputRequired(), 
		# Length(min=6, max=32, message="Password must be at least 6 characters long and no more than 32")
	])
	rememberMe = BooleanField('Remember Me')
	submit = SubmitField('Log In')


class LoginFormValidator:
	def __init__(self, email: str, password: str):
		self.email = email
		self.password = password

	def validateEmail(self) -> tuple:
		emailPattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
		if not emailPattern.match(self.email):
			return False, "Incorrect email"
		return True, "Successful email validate"

	def validatePassword(self) -> tuple:
		if len(self.password) < 8 or len(self.password) > 32 or not any(char.isdigit() for char in self.password) or not any(char.isalpha() for char in self.password):
			return False, "Password must be at least from 8 to 32 characters long"
		if not any(char.isdigit() for char in self.password) or not any(char.isalpha() for char in self.password):
			return False, "Password must contain at least one digit or letter"
		return True, "Successful password validate"

	def validateForm(self) -> tuple:
		emailValidation = self.validateEmail()
		if not emailValidation:
			return emailValidation 
		passwordValidation = self.validatePassword()
		if not passwordValidation:
			return passwordValidation
		return True, "Successful logging in"
