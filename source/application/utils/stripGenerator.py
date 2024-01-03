from random import randint
class StripGenerator():
	"""A class for generating codes, id's etc."""
	__symbols = "0123456789"

	@staticmethod
	def basicGenerator(symbols, lenght) -> str:
		output = []
		for _ in range(lenght):
			output.append(str(symbols[randint(0,9)]))
		return "".join(output)

	@staticmethod
	def generateConfirmationCode() -> str:

		code = StripGenerator().basicGenerator(StripGenerator.__symbols, 6)
		return code
	
	@staticmethod
	def generateUID() -> str:

		output = StripGenerator().basicGenerator(StripGenerator.__symbols, 10)
		output = list(output)
		output[0] = str(randint(1, 9))
		output = "".join(output)
		return output
	@staticmethod
	def generateCardID() -> str:

		output = StripGenerator().basicGenerator(StripGenerator.__symbols, 16)
		output = list(output)
		output[0] = str(randint(1, 9))
		output = "".join(output)
		return output
