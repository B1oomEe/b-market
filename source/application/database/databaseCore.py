from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

from .databaseModels import User, Card

from ..config import config


class PostgresDatabase():
	def __init__(self):
		try:
			self.engine = create_engine(
				url = config.DATABASE_URL_psycopg,
				echo = False
			)
			self.Session = sessionmaker(bind=self.engine)
			print("Created engine for database successfully.")
		except Exception as e:
			print(f"Error: Unable to create engine for database.\n{e}")
			raise  # Reraise the exception to let the caller handle it

		

	def getUserDataByField(self, fieldName: str, value) -> list | dict | None:
		with self.Session() as session:
			try:
				user = session.query(User).filter(getattr(User, fieldName) == value).first()
				return user
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}
	
	def getUserDataByEmail(self, userEmail: str) -> list | dict | None:
		try:
			with self.engine.connect() as connection:
				result = connection.execute(text(f"SELECT * FROM users WHERE email = '{userEmail}';"))
				return result.all()
		except SQLAlchemyError as error:
			return {
				"message": "Internal database error",
				"error": True,
				"errorLog": str(error)
			}
		except Exception as error:
			return {
				"message": "Data validation fail",
				"error": True,
				"errorLog": str(error)
			}

	def insertNewUser(self, data: dict) -> dict | None:
		with self.Session() as session:
			try:
				newUser = User(**data)
				session.add(newUser)
				session.commit()
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}

	def deleteUserByUID(self, uid: str) -> dict | None:
		with self.Session() as session:
			try:
				user = session.query(User).filter_by(uid=uid).first()
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}
			else:
				if user:
					session.delete(user)
					session.commit()

	def updateUserData(self, uid: str, dataDict: dict) -> dict | None:
		with self.Session() as session:
			try:
				user = session.query(User).filter_by(uid=uid).first()
				if user:
					for key, value in dataDict.items():
						setattr(user, key, value)
					session.commit()
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}
				

	def insertNewCard(self, data: dict) -> dict | None:
		with self.Session() as session:
			try:
				newCard = Card(**data)
				session.add(newCard)
				session.commit()
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}

	def getCardByCID(self, cid: str) -> list | dict | None:
		with self.Session() as session:
			try:
				card = session.query(Card).filter_by(cid=cid).first()
				if card:
					return card
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}

	def deleteCardByCID(self, cid: str) -> dict | None:
		with self.Session() as session:
			try:
				card = session.query(Card).filter_by(cid=cid).first()
				if card:
					session.delete(card)
					session.commit()
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}

	def getCardsByUID(self, uid: str) -> list | dict | None:
		with self.Session() as session:
			try:
				user = session.query(User).filter_by(uid=uid).first()
				if user:
					return user.cards
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}

	def getCardsByKeyword(self, keyword: str) -> list | dict | None:
		with self.Session() as session:
			try:
				cards = session.query(Card).filter(Card.name.like(f'%{keyword}%')).all()
				if cards:
					return cards
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}

	def getCardsByRandom(self) -> list | dict | None:
		with self.Session() as session:
			try:
				random_cards = (
					session.query(Card)
					.order_by(func.random())
					.limit(20)
					.all()
				)

				if random_cards:
					return random_cards

			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}

			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}
		
	def getCardsByRandomWithTarget(self, target: str) -> list | dict | None:
		with self.Session() as session:
			try:
				random_cards = (
					session.query(Card)
					.filter_by(target=target)
					.order_by(func.random())
					.limit(20)
					.all()
				)
	
				if random_cards:
					return random_cards
	
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
	
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}
	
	def updateCardPrice(self, cid: str, price: int) -> dict | None:
		with self.Session() as session:
			try:
				card = session.query(Card).filter_by(cid=cid).first()
				if card:
					card.price_usd = price
					session.commit()
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}

	def closeCard(self, cid: str) -> dict | None:
		with self.Session() as session:
			try:
				card = session.query(Card).filter_by(cid=cid).first()
				if card:
					card.is_closed = True
					session.commit()
			except SQLAlchemyError as error:
				return {
					"message": "Internal database error",
					"error": True,
					"errorLog": str(error)
				}
			except Exception as error:
				return {
					"message": "Data validation fail",
					"error": True,
					"errorLog": str(error)
				}