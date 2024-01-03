from flask import Flask
from flask_wtf.csrf import CSRFProtect
from ..config import config
from flask_session import Session

def createApp(name, template_folder, static_folder):
	# The templates and static folder is the path to the `templates` and `static` relative to the file where `createApp()` is used
	app = Flask(name, template_folder=template_folder, static_folder=static_folder) 
	app.config.from_object(config)
	app.secret_key = app.config['SECRET_KEY']
	_csrf = CSRFProtect(app)
	Session(app)
	return app