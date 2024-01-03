from flask import Blueprint, make_response, render_template, session, request
from sqlalchemy.exc import SQLAlchemyError

from .. import auth, database, login_manager

essentialController = Blueprint('essentialController', __name__)

@login_manager.user_loader
def load_user(user_id):
	# Here needs to implement code that loads the user from your database by user_id
	return user_id

@essentialController.errorhandler(404)
def pageNotFound(error):
	return "Page not found", 404

@essentialController.route('/', methods=['GET'])
def index():
	return render_template('welcomePage.html')


@essentialController.route('/home', methods=['GET'])
@auth.tokenRequired
def homePage():
	dataFromDataBase = database.getCardsByRandom()
	return render_template('homePage.html', cards=dataFromDataBase)
