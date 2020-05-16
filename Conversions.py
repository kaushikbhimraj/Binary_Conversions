"""
Basic Conversions
"""
from ErrorHandling import Checks

class Conversions(Checks):
	"""
	Performs 2 conversions. 
	binary(number):  Decimal -> Binary
	decimal(binary): Binary  -> Decimal
	"""

	def __init__(self):
		self.binn = ""

	
	def binary(self, num) -> str:
		""" Check sign bit before converting to decimal. """
		
		self.checkIntValue(num)
		if num < 0:
			isNeg     = True
			self.binn = ""
			self.binary_helper((-1)*num)
			return "1"+self.binn
		else:
			isNeg     = False
			self.binn = ""
			self.binary_helper(num)
			return "0"+self.binn


	def binary_helper(self, num):
		""" Convert from a decimal(int) to binary(string)."""
		
		if not num:
			return
		self.binary_helper(num>>1)
		self.binn += str(num&1)


	def decimal(self, binn=None) -> int:
		""" Check sign bit before converting to binary."""

		self.checkStrValue(binn)
		if binn[0]=="1":
			return (-1)*self.decimal_helper(binn[1:],0)
		return self.decimal_helper(binn[1:],0)


	def decimal_helper(self, binn, temp):
		""" Convert from binary (string) to decimal(int)."""
		
		if not binn:
			return temp
		if binn[0] == "1":
			temp += 2**(len(binn)-1)
		return self.decimal_helper(binn[1:], temp)


"""
x = Conversions()
print(x.binary(-147))
print(x.decimal("010010011"))

"""


