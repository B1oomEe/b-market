from application.utils.startLog import startLog
from application.controllers.essentialController import *
from application.controllers.userController import *
from application.controllers.cardController import *
from application.controllers.authController import *
from application.__init__ import *


def main():
	app.register_blueprint(userController, url_prefix='/user')
	app.register_blueprint(cardController, url_prefix='/cards')
	app.register_blueprint(essentialController, url_prefix='/')
	app.register_blueprint(authController, url_prefix='/auth')
	
	app.secret_key = app.config['SECRET_KEY']
	
	startLog(app.config['DB_PORT'], app.config['DB_HOST'], app.config['DB_NAME'], app.config['DB_USER'])
	app.run(debug=app.config['DEBUG'])

if __name__ == '__main__':
	main()