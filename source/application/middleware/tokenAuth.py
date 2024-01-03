from functools import wraps
from flask import request, jsonify
import jwt
from datetime import datetime, timedelta

class JWTAuth():
	def __init__(self, secret_key, jwt_expiration_time_sec):
		self.__secret_key = secret_key
		self.__jwt_expiration_time_sec = int(jwt_expiration_time_sec)

	def tokenGenerator(self, login):
		return jwt.encode({
			'user': login,
			'expiration': str(datetime.now() + timedelta(seconds=self.__jwt_expiration_time_sec))
		}, self.__secret_key)

	def tokenRequired(self, function):
		@wraps(function)
		def decorated(*args, **kwargs):
			token = request.cookies.get('token')
			if not token:
				return jsonify({
					"message": "token is missing",
					"data": None,
					"error": "Unauthorized"
				}), 401
			try:
				jwt.decode(str(token), self.__secret_key, algorithms=["HS256"])
			except Exception as error:
				return jsonify({
					"message": "token is invalid",
					"data": None,
					"error": "Unauthorized"
				}), 403
			return function(*args, **kwargs)
		return decorated
