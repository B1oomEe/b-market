from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os


load_dotenv()
class Config(BaseSettings):
	SECRET_KEY: str # Secret key for sessions and encryption
	SESSION_COOKIE_HTTPONLY: str
	SESSION_TYPE: str
	SESSION_TIME: int
	DB_PORT: int
	DB_HOST: str
	DB_NAME: str
	DB_USER: str
	DB_PASSWORD: str
	DEBUG: bool # Debug mode
	
	@property
	def DATABASE_URL_asyncpg(self):
		
		# DSN - postgresql+asyncpg://postgres:postgres@localhost:5432/sa
		return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
	
	@property
	def DATABASE_URL_psycopg(self):
		# DSN - postgresql+psycopg://postgres:postgres@localhost:5432/sa
		return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
	
config = Config()
