from flask import render_template, request, redirect, url_for, make_response, session
from flask_login import login_user, current_user, logout_user, login_required


from ..__init__ import app, auth, database, login_manager
from ..validation.registrationValidation import RegistrationForm
from ..validation.newCardValidation import NewCardForm
from ..validation.loginValidation import LoginForm
from ..utils.stripGenerator import StripGenerator


##################### GET METHODS #####################

@login_manager.user_loader
def load_user(user_id):
	# Here needs to implement code that loads the user from your database by user_id
	return user_id

@app.route('/', methods=['GET'])
def index():
	return render_template('welcomePage.html')

@app.route('/registration', methods=['GET'])
def registrationPage():
	if request.cookies.get('token'):
		return redirect(url_for('homePage'))
		
	form = RegistrationForm()
	return render_template('registrationPage.html', form=form)

@app.route('/login', methods=['GET'])
def loginPage():
	if request.cookies.get('token'):
		return redirect(url_for('homePage'))
	form = LoginForm()
	return render_template('loginPage.html', form=form)

@app.route('/mycards', methods=['GET'])
@auth.tokenRequired
def mycardsPage():
	return render_template('myCardsPage.html')

@app.route('/liked', methods=['GET'])
@auth.tokenRequired
def likedPage():
	return render_template('likedPage.html')

@app.route('/settings', methods=['GET'])
@auth.tokenRequired
def settingsPage():
	return render_template('settingsPage.html')

@app.route('/chats', methods=['GET'])
@auth.tokenRequired
def chatsPage():
	return render_template('chatsPage.html')

@app.route('/logout', methods=['GET'])
@auth.tokenRequired
def logOutPage():
	logout_user()
	response = make_response(redirect(url_for('loginPage')))
	response.delete_cookie('token')
	session.pop('userID', None)
	return response

@app.errorhandler(404)
def pageNotFound(error):
	return "Page not found", 404


@app.route('/newcard', methods=['GET'])
@auth.tokenRequired
def newCardPage():
	form = NewCardForm()
	return render_template('addCardPage.html', form=form)

@app.route('/home', methods=['GET'])
@auth.tokenRequired
def homePage():
	userID = session.get('userID')
	cardsID = database.getCardsByUID(userID)
	cardsOutput = []
	print(userID)
	for x in cardsID: # Getting test cards from database with predefined cards id
		card = database.getCardByCID(str(x))
		if card:
			cardsOutput.append(card)
	return render_template('homePage.html', cards=cardsOutput)

##################### POST METHODS #####################

@app.route('/user/<username>')
@auth.tokenRequired
def showUser(username):
	pass

@app.route('/profile', methods=['POST'])
@auth.tokenRequired
def profile():
	pass


@app.route('/home', methods=['POST'])
@auth.tokenRequired
def homePageProcess():
	userID = session.get('userID')
	dataFromDataBase = database.getUserDataByField("uid", userID)
	return render_template('homePage.html', data=dataFromDataBase)


@app.route('/registration', methods=['POST'])
def submitRegistrationForm():
	if request.cookies.get('token'):
		return redirect(url_for('homePage'))
	data = request.form.to_dict(flat=True)
	form = RegistrationForm()

	if form.validate_on_submit():
		def findUniqueUserUid():
			userID = StripGenerator.generateUID()
			if database.getUserDataByField("uid", userID):
				return findUniqueUserUid()
			return userID
		uniqueUserUid = findUniqueUserUid()
	
		dataForDatabase = (uniqueUserUid, data['email'], data['password'], data['username'], data['contact_email'], '', '', '', '')
		newUser = database.insertNewUser(dataForDatabase)
		if newUser: # catching errors
			pass
		else:
			token = auth.tokenGenerator(data['email'])
			response = make_response(redirect(url_for('homePage')))
			response.set_cookie('token', token)
			session['userID'] = uniqueUserUid
			return response
	
	return render_template('registrationPage.html', form=form)


@app.route('/login', methods=['POST'])
def submitLoginForm():
	if request.cookies.get('token'):
		return redirect(url_for('homePage'))
	form = LoginForm()
	data = request.form.to_dict(flat=True)

	userDataFromDatabase = database.getUserDataByEmail(data['email'])
	if form.validate_on_submit() and userDataFromDatabase:
		if data['email'] == userDataFromDatabase[3] and data['password'] == userDataFromDatabase[4]:
			token = auth.tokenGenerator(data['email'])
			response = make_response(redirect(url_for('homePage')))
			response.set_cookie('token', token)
			session['userID'] = userDataFromDatabase[1]
			return response
	return render_template('loginPage.html', form=form)


@app.route('/newcard', methods=['POST'])
@auth.tokenRequired
def newCardProcessPage():
	form = NewCardForm()
	userID = session.get('userID')
	if form.validate_on_submit():
		cardID = StripGenerator.generateCardID()
		data = (cardID, form.title.data, userID, form.category.data, form.purpose.data, False, form.price.data, form.description.data, 0, [form.photos.data])

		userData = list(database.getUserDataByUID(str(userID)))
		userCardsAlreadyExists = userData[9]
		userCardsAlreadyExists.append(cardID)
		userCardsAlreadyExists = ", ".join(userCardsAlreadyExists)
		print(userCardsAlreadyExists)

		updateUserData = database.updateUserData(userID, {'cards': userCardsAlreadyExists})
		newCard = database.insertNewCard(data)
		return redirect(url_for('homePage'))

	return render_template('addCardPage.html', form=form)