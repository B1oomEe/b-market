from flask import render_template, request, redirect, url_for, make_response, session, Blueprint

from ..__init__ import auth, database, login_manager
from ..validation.newCardValidation import NewCardForm, CardFormValidator
from ..utils.stripGenerator import StripGenerator
from ..utils.notificationsClassification import *

cardController = Blueprint('cardController', __name__)

@login_manager.user_loader
def load_user(user_id):
	return user_id

@cardController.route('/newcard', methods=['GET'])
@auth.tokenRequired
def newCardPage():
	form = NewCardForm()
	return render_template('addCardPage.html', form=form)

@cardController.route('/home', methods=['GET'])
@auth.tokenRequired
def homePage():
	userID = session.get('userID')
	cardsID = database.getCardsByUID(userID)
	cardsOutput = []
	for x in cardsID:
		card = database.getCardByCID(str(x))
		if card:
			cardsOutput.append(card)
	return render_template('homePage.html', cards=cardsOutput)


@cardController.route('/newcard', methods=['POST'])
@auth.tokenRequired
def newCardPageProcess():
	form = NewCardForm()
	data = request.form.to_dict(flat=True)
	

	if form.validate_on_submit():
		for field in ('csrf_token', 'title', 'category', 'purpose', 'stage', 'description', 'price', 'photos'):
			if field not in list(data.keys()):
				print(list(data.keys()))
				return render_template('addCardPage.html', form=form, error=ClientErrorNotification("Form field names error", "Try to update this page to fix this problem"))
		
		isFormValid = CardFormValidator(data['title'], data['category'], data['purpose'], data['stage'], data['description'], data['price'], data['photos']).validateForm() # Checking form for validity
		if isFormValid: # Checking form valid status
			return render_template('addCardPage.html', form=form, error=ValidationErrorNotification(isFormValid['field'], isFormValid['message']))
		
		
		def findUniqueCardUid():
			cardID = StripGenerator.generateCardID()
			if database.getUserDataByField("uid", cardID):
				return findUniqueCardUid()
			return cardID
		uniqueCardUid = findUniqueCardUid()

		dataForDatabase = {
			"cid": uniqueCardUid,
			"name": data['title'],
			"owner_id": session['userID'],
			"category": data['category'],
			"target": data['purpose'],
			"price_usd": data['price'],
			"description": data['description'],
			"images": data['photos'],
			"stage": data['stage']
		}

		userID = session['userID']
		dataFromDataBase = database.getUserDataByField("uid", userID)
	
		newCards = dataFromDataBase.cards
		newCards.append(uniqueCardUid)

		database.updateUserData(userID, {"cards": newCards})
		database.insertNewCard(dataForDatabase)

		response = make_response(redirect(url_for('essentialController.homePage')))
		
		
		return response

	return render_template('addCardPage.html', form=form)
