from flask import Blueprint, render_template, request, redirect, url_for, make_response, session
from flask_login import login_user, current_user, logout_user, login_required


from .. import database, auth # , login_manager
from ..validation.registrationValidation import RegistrationForm, RegistrationFormValidator
from ..validation.loginValidation import LoginForm, LoginFormValidator
from ..utils.stripGenerator import StripGenerator
from ..auth.checkHash import PasswordManager
from ..utils.notificationsClassification import *


authController = Blueprint('authController', __name__)

# @login_manager.user_loader
# def load_user(user_id):
# 	return user_id


@authController.route('/registration', methods=['GET'])
def registrationPage():
	if request.cookies.get('token'):
		return redirect(url_for('essentialController.homePage'))

	form = RegistrationForm()
	return render_template('registrationPage.html', form=form)


@authController.route('/login', methods=['GET'])
def loginPage():
	if request.cookies.get('token'):
		return redirect(url_for('essentialController.homePage'))
	
	form = LoginForm()
	return render_template('loginPage.html', form=form)


@authController.route('/login', methods=['POST'])
def submitLoginForm():
	form = LoginForm()
	data = request.form.to_dict(flat=True)
	
	if form.validate_on_submit():
		for field in ('csrf_token', 'email', 'password', 'submit'):
			if field not in list(data.keys()):
				return render_template('loginPage.html', form=form, error=ClientErrorNotification("Form field names error", "Try to update this page to fix this problem"))
		
		isFormValid = LoginFormValidator(data['email'], data['password']).validateForm() # Checking form for validity
		if not isFormValid[0]: # Checking form valid status (isFormValid looks like: (False, "message error") or (True, "success"))
			print(isFormValid)
			return render_template('loginPage.html', form=form, error=ValidationErrorNotification(isFormValid[0], isFormValid[1]))
		
		userDataFromDatabase = database.getUserDataByEmail(data['email']) # Getting user data from the database if form valid
		if not userDataFromDatabase: # Checking whether user exists
			return render_template('loginPage.html', form=form, error=ValidationErrorNotification("email", "User with this email doesn't exists"))
		
		if "error" in userDataFromDatabase: # Checking for errors in database response
			print(userDataFromDatabase)
			return render_template('loginPage.html', form=form, error=ServerErrorNotification("DATABASE ERROR", f"{userDataFromDatabase['message']}"))
		
		userDataFromDatabase = userDataFromDatabase[0]
		if not PasswordManager.verifyPassword(data['password'], userDataFromDatabase[4]):
			return render_template('loginPage.html', form=form, error=ValidationErrorNotification("password", "Incorrect password"))
		
		token = auth.tokenGenerator(data['email']) # Creating JWT-token
		response = make_response(redirect(url_for('essentialController.homePage')))
		response.set_cookie('token', token, path="/", expires=15_552_000) # Setting JWT-token in cookies | Expires 15_552_000 seconds = ~180 Days
		
		if request.form.get('rememberMe'): # If users sets Remember Me field to yes, we create cookies with his user id
			response.set_cookie('userID', userDataFromDatabase[1], path='/', expires=15_552_000)  # Expires 15_552_000 seconds = ~180 Days
		
		session['userID'] = userDataFromDatabase[1] # Setting user ID in browser session
		session['token'] = token
		return response

	return render_template('loginPage.html', form=form)


@authController.route('/registration', methods=['POST'])
def submitRegistrationForm():
	data = request.form.to_dict(flat=True)
	form = RegistrationForm()
	
	if form.validate_on_submit():
		for field in ('csrf_token', 'username', 'email', 'contact_email', 'password', 'confirm_password', 'submit'):
			if field not in list(data.keys()):
				return render_template('registrationPage.html', form=form, error=ClientErrorNotification("Form field names error", "Try to update this page to fix this problem")) 
		
		isFormValid = RegistrationFormValidator(data['username'], data['email'], data['contact_email'], data['password'], data['confirm_password']).validateForm() # Checking form for validity
		
		if not isFormValid[0]:
			return render_template('registrationPage.html', form=form, error=isFormValid)
		
		isUserWithThatEmaiExists = database.getUserDataByEmail(data['email'])
		if isUserWithThatEmaiExists:
			return render_template('registrationPage.html', form=form, error=ValidationErrorNotification("email", "User with this email already exists"))
		
		def findUniqueUserUid():
			userID = StripGenerator.generateUID()
			if database.getUserDataByField("uid", userID):
				return findUniqueUserUid()
			return userID
		uniqueUserUid = findUniqueUserUid()

		dataForDatabase = {
			"uid": uniqueUserUid,
			"email": data['email'],
			"password": PasswordManager.hashPassword(data['password']),
			"owner_name": data['username'],
			"contact_email": data['contact_email']
		}

		newUser = database.insertNewUser(dataForDatabase)
		if newUser: # catching errors
			return render_template('registrationPage.html', form=form, error=ServerErrorNotification("Critical error, while inserting new user", f"Error: {newUser['message']}"))

		token = auth.tokenGenerator(data['email'])
		response = make_response(redirect(url_for('essentialController.homePage')))
		response.set_cookie('token', token, path='/', expires=15_552_000) # Expires 15_552_000 seconds = ~180 Days
		session['userID'] = uniqueUserUid

		session['token'] = token

		return response
	
	return render_template('registrationPage.html', form=form)