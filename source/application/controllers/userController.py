from flask import Blueprint, render_template, request, redirect, url_for, make_response, session
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.exc import SQLAlchemyError

from .. import auth, database, login_manager
from ..validation.registrationValidation import RegistrationForm
from ..validation.loginValidation import LoginForm
from ..utils.stripGenerator import StripGenerator

userController = Blueprint('userController', __name__)

@login_manager.user_loader
def load_user(user_id):
	return user_id

@userController.route('/profile', methods=['POST'])
@auth.tokenRequired
def profile():
    pass

@userController.route('/mycards', methods=['GET'])
@auth.tokenRequired
def mycardsPage():
	try:
		userID = session['userID']
		dataFromDataBase = database.getUserDataByField("uid", userID)
	except SQLAlchemyError as error:
		return {
			"message": "Internal database error",
			"error": True,
			"errorLog": str(error)
		}
	else:
		cards = []
		for card in dataFromDataBase.cards:
			cards.append(database.getCardByCID(card))
		return render_template('myCardsPage.html', cards=cards)

@userController.route('/liked', methods=['GET'])
@auth.tokenRequired
def likedPage():
	return render_template('likedPage.html')

@userController.route('/settings', methods=['GET'])
@auth.tokenRequired
def settingsPage():
	return render_template('settingsPage.html')

@userController.route('/chats', methods=['GET'])
@auth.tokenRequired
def chatsPage():
	return render_template('chatsPage.html')

@userController.route('/logout', methods=['GET'])
@auth.tokenRequired
def logOutPage():
	logout_user()
	response = make_response(redirect(url_for('authController.loginPage')))
	response.delete_cookie('token', path='/')
	response.delete_cookie('userID', path='/')
	session.pop('userID', None)
	return response