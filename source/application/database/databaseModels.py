from sqlalchemy import Table, Column, Integer, String, MetaData, DATE, ARRAY, TEXT, VARCHAR, CHAR, BOOLEAN, REAL
from sqlalchemy.ext.declarative import declarative_base
import datetime

metadataObj = MetaData()
Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column("id", Integer, primary_key = True)
	uid = Column("uid", CHAR(10))
	create_date = Column("create_date", DATE, default = str(datetime.date.today()))
	email = Column("email", VARCHAR(50))
	password = Column("password", VARCHAR(512))
	owner_name = Column("owner_name", VARCHAR(32))
	contact_email = Column("contact_email", VARCHAR(50))
	description = Column("description", VARCHAR(500), default = None)
	additional_contacts = Column("additional_contacts", ARRAY(VARCHAR), default = None)
	cards = Column("cards", ARRAY(VARCHAR), default = None)
	bookmarks = Column("bookmarks", ARRAY(VARCHAR), default = None)
	role = Column("role", VARCHAR(100), default = None)

class Card(Base):
	__tablename__ = 'cards'

	id = Column(Integer, primary_key = True)
	cid = Column(VARCHAR(16))
	create_date = Column(DATE, default = str(datetime.date.today()))
	name = Column(VARCHAR(40))
	owner_id = Column(VARCHAR(10))
	category = Column(VARCHAR(200))
	target = Column(VARCHAR(50))
	is_closed = Column(BOOLEAN, default = False)
	price_usd = Column(REAL)
	description = Column(VARCHAR(200), default = None)
	bookmarks_count = Column(Integer, default = 0)
	images = Column(ARRAY(String), default = None)
	stage = Column(CHAR(150), default = None)
