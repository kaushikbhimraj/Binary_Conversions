
"""
Error Handling
"""

class Checks:

	def checkStrValue(self, string):
		if type(string) != str or not string:
			raise TypeError("Either string is empty or not a string.")

	def checkIntValue(self, integer):
		if type(integer) != int:
			raise TypeError("Must be an integer.")