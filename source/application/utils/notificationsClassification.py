class AppError(Exception):
	"""The base class for all errors in the application."""

	def __init__(self, message, level="error"):
		self.message = message
		self.level = level
		super().__init__(message)

	def getContent(self):
		return (self.message, self.level)

class ValidationErrorNotification(AppError):
	"""A class for validation errors."""

	def __init__(self, field: str, message: str):
		super().__init__(message, level="error")
		self.field = field

	def getContent(self):
		return (*super().getContent(), self.field, self.message)

class ServerErrorNotification(AppError):
	"""A class for server-related errors."""

	def __init__(self, code: str, message: str):
		super().__init__(message, level="error")
		self.code = code

	def getContent(self):
		return (*super().getContent(), self.code)

class ClientErrorNotification(AppError):
	"""A class for client-related errors."""

	def __init__(self, header: str, message: str):
		super().__init__(message, level="error")
		self.header = header

	def getContent(self):
		return (*super().getContent(), self.header)

class InfoNotification(AppError):
	"""A class for infrastructure errors related to configuration or environment."""

	def __init__(self, header: str, message: str):
		super().__init__(message, level="info")
		self.header = header

	def getContent(self):
		return (*super().getContent(), self.header)