from flask import Blueprint, make_response, render_template, session, request, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError

from .. import auth, database # , login_manager
from ..utils.graphicMaker import ReportEmailSender

essentialController = Blueprint('essentialController', __name__)

# @login_manager.user_loader
# def load_user(user_id):
# 	# Here needs to implement code that loads the user from your database by user_id
# 	return user_id

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
	if dataFromDataBase == None: dataFromDataBase = []
	print(dataFromDataBase)
	return render_template('homePage.html', cards=dataFromDataBase)

@essentialController.route('/lookforinvestor', methods=['GET'])
@auth.tokenRequired
def lookforinvestorPage():
	dataFromDataBase = database.getCardsByRandomWithTarget('Инвестирование')
	if dataFromDataBase == None: dataFromDataBase = []
	return render_template('lookForInvestments.html', cards=dataFromDataBase)

@essentialController.route('/buysubscription', methods=['GET'])
@auth.tokenRequired
def buySubscriptionPage():
	return render_template('buySubscriptionPage.html')

@essentialController.route('/getEmailInfo', methods=['POST'])
@auth.tokenRequired
def getEmailInfo():
	userEmail = database.getUserDataByField("uid", session.get('userID')).email
	cardID = request.form.get('argument')
	dataAboutCard = database.getCardByCID(cardID)
	obj = ReportEmailSender()
	obj.sendEmailWithPlots(f"Info about {dataAboutCard.name}", dataAboutCard.description, userEmail)
	dataFromDataBase = database.getCardsByRandom()
	return render_template('homePage.html', cards=dataFromDataBase)

@essentialController.route('/toLike', methods=['POST'])
@auth.tokenRequired
def toLike():
	cardID = request.form.get('argument')
	dataFromDataBase = database.getUserDataByField("uid", session.get('userID'))
	cardInDataBase = database.getCardByCID(cardID)
	database.updateCardData(cardID, {"bookmarks_count": cardInDataBase.bookmarks_count + 1})
	if dataFromDataBase.bookmarks is None:
		newCards = [cardID]
	else:
		newCards = dataFromDataBase.bookmarks
		newCards.append(cardID)
	database.updateUserData(session.get('userID'), {"bookmarks": newCards})
	return render_template('homePage.html', cards=newCards)