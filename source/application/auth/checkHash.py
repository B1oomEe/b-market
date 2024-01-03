import bcrypt

class PasswordManager:
	"""Class for hashing and matching passwords via bcrypt"""
	def hashPassword(password: str):
		# Using Bcrypt for password hashing
		hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
		return hashedPassword.decode('utf-8')
	
	def verifyPassword(inputPassword: str, hashedPassword: str):
		# Checking the match between the entered password and the hash in the database using Bcrypt
		try:
			isVerified = bcrypt.checkpw(inputPassword.encode('utf-8'), hashedPassword.encode('utf-8'))
		except:
			return False
		
		return isVerified
