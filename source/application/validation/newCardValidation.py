from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, FileField, BooleanField


class NewCardForm(FlaskForm):
	title = StringField('Title')
	category = SelectField('Category', 
		choices=[
		('', 'Select category'),
		('Grocery Stores', 'Grocery Stores'), 
		('Clothing and Footwear', 'Clothing and Footwear'), 
		('Electronics and Appliances', 'Electronics and Appliances'), 
		('Cosmetics and Perfumes', 'Cosmetics and Perfumes'), 
		('Automotive Parts and Accessories', 'Automotive Parts and Accessories'), 
		('Restaurants', 'Restaurants'), 
		('Cafes', 'Cafes'), 
		('Bars and Nightclubs', 'Bars and Nightclubs'), 
		('Fast Food', 'Fast Food'), 
		('Catering Services', 'Catering Services'), 
		('Food Industry', 'Food Industry'), 
		('Machinery and Engineering', 'Machinery and Engineering'), 
		('Chemical Industry', 'Chemical Industry'), 
		('Electronics and Microelectronics', 'Electronics and Microelectronics'), 
		('Wood Processing Industry', 'Wood Processing Industry'), 
		('Restaurant Chains', 'Restaurant Chains'), 
		('Stores and Retail Franchises', 'Stores and Retail Franchises'), 
		('Fitness Centers', 'Fitness Centers'), 
		('Educational Franchises', 'Educational Franchises'), 
		('Medical Franchises', 'Medical Franchises'), 
		('Software Development', 'Software Development'), 
		('Internet Technologies and E-Commerce', 'Internet Technologies and E-Commerce'), 
		('Medical and Biotechnology Startups', 'Medical and Biotechnology Startups'), 
		('Energy Technologies', 'Energy Technologies'), 
		('Artificial Intelligence and Machine Learning', 'Artificial Intelligence and Machine Learning'), 
		('Banks and Financial Institutions', 'Banks and Financial Institutions'), 
		('Insurance Companies', 'Insurance Companies'), 
		('Investment Funds', 'Investment Funds'), 
		('Financial Consultations', 'Financial Consultations'), 
		('Tax and Legal Services', 'Tax and Legal Services'), 
		('Commercial Real Estate', 'Commercial Real Estate'), 
		('Hotels and Motels', 'Hotels and Motels'), 
		('Apartments and Residential Complexes', 'Apartments and Residential Complexes'), 
		('Shopping Centers', 'Shopping Centers'), 
		('Manufacturing Facilities', 'Manufacturing Facilities'), 
		('Legal Services', 'Legal Services'), 
		('Marketing and Advertising Agencies', 'Marketing and Advertising Agencies'),
		('Engineering and Architectural Consultations', 'Engineering and Architectural Consultations'), 
		('Information Technologies', 'Information Technologies'), 
		('Educational Services', 'Educational Services'), 
		('Medical Clinics', 'Medical Clinics'), 
		('Dental Clinics', 'Dental Clinics'), 
		('Pharmaceutical Companies', 'Pharmaceutical Companies'), 
		('Medical Equipment', 'Medical Equipment'), 
		('Laboratories and Diagnostic Centers', 'Laboratories and Diagnostic Centers'), 
		('Crop Farming', 'Crop Farming'), 
		('Livestock Farming', 'Livestock Farming'), 
		('Agrotourism', 'Agrotourism'), 
		('Agricultural Machinery Production', 'Agricultural Machinery Production'), 
		('Logging and Wood Processing', 'Logging and Wood Processing')
	])

	purpose = SelectField('Purpose of Sale', choices=[
		('', 'Select Purpose' ),
		('Investment', 'Investment'), 
		('Buy', 'Buy'), 
		('Finding partners', 'Finding partners'), 
		('Looking for buy/invest offers', 'Looking for buy/invest offers'), 
		('Looking for partnership', 'Looking for partnership'), 
		('Looking for loan offers', 'Looking for loan offers')
	])
	stage = SelectField('Stage', choices=[
		('', 'Select Stage'),
		('Idea', 'Idea'),
		('Startup (have a team)', 'Startup (have a team)'),
		('Constant profit', 'Constant profit'),
		('No profit', 'No profit')
	])
	description = TextAreaField('Description')
	price = StringField('Price')
	photos = FileField('Photos')
	waitForInvest = BooleanField('Looking for investments?')

class CardFormValidator():
	def __init__(self, title: str, category: str, purpose: str, stage: str, description: str, price: str, photos: str):
		self.title = title
		self.category = category
		self.purpose = purpose
		self.stage = stage
		self.description = description
		self.price = price
		self.photos = photos

		self.categories = [
		    'Grocery Stores',
		    'Clothing and Footwear',
		    'Electronics and Appliances',
		    'Cosmetics and Perfumes',
		    'Automotive Parts and Accessories',
		    'Restaurants',
		    'Cafes',
		    'Bars and Nightclubs',
		    'Fast Food',
		    'Catering Services',
		    'Food Industry',
		    'Machinery and Engineering',
		    'Chemical Industry',
		    'Electronics and Microelectronics',
		    'Wood Processing Industry',
		    'Restaurant Chains',
		    'Stores and Retail Franchises',
		    'Fitness Centers',
		    'Educational Franchises',
		    'Medical Franchises',
		    'Software Development',
		    'Internet Technologies and E-Commerce',
		    'Medical and Biotechnology Startups',
		    'Energy Technologies',
		    'Artificial Intelligence and Machine Learning',
		    'Banks and Financial Institutions',
		    'Insurance Companies',
		    'Investment Funds',
		    'Financial Consultations',
		    'Tax and Legal Services',
		    'Commercial Real Estate',
		    'Hotels and Motels',
		    'Apartments and Residential Complexes',
		    'Shopping Centers',
		    'Manufacturing Facilities',
		    'Legal Services',
		    'Marketing and Advertising Agencies',
		    'Engineering and Architectural Consultations',
		    'Information Technologies',
		    'Educational Services',
		    'Medical Clinics',
		    'Dental Clinics',
		    'Pharmaceutical Companies',
		    'Medical Equipment',
		    'Laboratories and Diagnostic Centers',
		    'Crop Farming',
		    'Livestock Farming',
		    'Agrotourism',
		    'Agricultural Machinery Production',
		    'Logging and Wood Processing'
		]

		self.purposes = [
			'Investment', 
			'Buy',
			'Finding partners',
			'Looking for buy/invest offers',
			'Looking for partnership', 
			'Looking for loan offers'
		]

		self.stages = [
			'Idea',
			'Startup (have a team)',
			'Constant profit',
			'No profit'
		]
		

	def validateTitle(self) -> None | dict:
		if not bool(self.title):
			return {
				"message": "Title is too long",
				"error": True,
				"field": "title"
			}
		if len(self.title) > 40:
			return {
				"message": "Title is too long",
				"error": True,
				"field": "title"
			}
		
	def validateCategory(self) -> None | dict:
		if self.category == '':
			return {
				"message": "Please, choose category",
				"error": True,
				"field": "category"
			}
		if self.category not in self.categories:
			return {
				"message": "Incorrect category",
				"error": True,
				"field": "category"
			}
		
	def validatePurpose(self) -> None | dict:
		if self.purpose == '':
			return {
				"message": "Please, choose target",
				"error": True,
				"field": "purpose"
			}
		if self.purpose not in self.categories:
			return {
				"message": "Incorrect target",
				"error": True,
				"field": "purpose"
			}
		
	def validateStage(self) -> None | dict:
		if self.stage == '':
			return {
				"message": "Please, choose stage",
				"error": True,
				"field": "stage"
			}
		if self.stage not in self.stages:
			return {
				"message": "Incorrect stage",
				"error": True,
				"field": "stage"
			}

	def validateDescription(self) -> None | dict:
		if not bool(self.description):
			return {
				"message": "Please add a description",
				"error": True,
				"field": "description"
			}
		if len(self.description) > 200:
			return {
				"message": "Description is too long",
				"error": True,
				"field": "description"
			}
		
	def validatePrice(self) -> None | dict:
		if not bool(self.price):
			return {
				"message": "Please set price",
				"error": True,
				"field": "price"
			}
		for char in str(self.price):
			if not char.isdigit():
				return {
					"message": "Incorrect price",
					"error": True,
					"field": "price"
				}
		
	def validatePhotos(self) -> None | dict:
		return


	def validateForm(self) -> dict | None:
		fields_to_validate = {
			'title': self.validateTitle,
			'category': self.validateCategory,
			'stage': self.validateStage,
			'description': self.validateDescription,
			'price': self.validatePrice,
			'photos': self.validatePhotos
		}

		for field_name, validation_function in fields_to_validate.items():
			validity = validation_function()
			if validity:
				return validity