from flask import render_template, request, redirect, url_for, make_response, session, Blueprint
import plotly.express as px
import pandas as pd

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
		# Проверяем наличие обязательных полей
		required_fields = ['csrf_token', 'title', 'category', 'purpose', 'stage', 'description', 'price', 'photos']
		if not all(field in data for field in required_fields):
			return render_template('addCardPage.html', form=form, error=ClientErrorNotification("Form field names error", "Try to update this page to fix this problem"))

		# Дополнительная валидация формы карточки
		isFormValid = CardFormValidator(data['title'], data['category'], data['purpose'], data['stage'], data['description'], data['price'], data['photos']).validateForm()
		if isFormValid:
			return render_template('addCardPage.html', form=form, error=ValidationErrorNotification(isFormValid['field'], isFormValid['message']))

		# Генерация уникального идентификатора карточки
		def findUniqueCardUid():
			cardID = StripGenerator.generateCardID()
			if database.getUserDataByField("uid", cardID):
				return findUniqueCardUid()
			return cardID
		uniqueCardUid = findUniqueCardUid()

		# Подготовка данных для сохранения в базе данных
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

		# Если пользователь не имеет карточек, создаем новый список с одной карточкой
		if dataFromDataBase.cards is None:
			newCards = [uniqueCardUid]
		else:
			newCards = dataFromDataBase.cards
			newCards.append(uniqueCardUid)

		# Обновление данных пользователя в базе данных
		database.updateUserData(userID, {"cards": newCards})

		# Вставка новой карточки в базу данных
		database.insertNewCard(dataForDatabase)

		# Перенаправление на домашнюю страницу
		return redirect(url_for('essentialController.homePage'))

	return render_template('addCardPage.html', form=form)
