"""
Unit Testing
"""

import unittest  
from Conversions import Conversions


class testConversions(unittest.TestCase):

	def testBinary(self):
		self.assertRaises(TypeError, Conversions().binary, "a")

	def testDecimal(self):
		self.assertRaises(TypeError, Conversions().decimal, "")
		self.assertRaises(TypeError, Conversions().decimal, 3)


	def testConv(self):
		self.assertEqual(Conversions().binary(147),"010010011")
		self.assertEqual(Conversions().binary(-147),"110010011")
		self.assertEqual(Conversions().decimal("010010011"),147)
		self.assertEqual(Conversions().decimal("110010011"),-147)


if __name__ == "__main__":
	unittest.main()
