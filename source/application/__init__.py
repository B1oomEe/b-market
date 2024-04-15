from flask_login import LoginManager

from application.utils.appCreator import createApp
from application.middleware.tokenAuth import JWTAuth
from application.database.databaseCore import PostgresDatabase

import dotenv
dotenv.load_dotenv()

app = createApp(__name__, 'templates', 'static') # The templates and static folder is the path to the `templates` and `static` relative to the `__init__.py`
auth = JWTAuth(app.config['SECRET_KEY'], app.config['SESSION_TIME'])
login_manager = LoginManager(app)
login_manager.init_app(app)
database = PostgresDatabase()