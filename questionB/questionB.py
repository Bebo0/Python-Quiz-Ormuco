from fractions import Fraction
"""Compares 2 string to see if they're numbers

"""
def comparable(str1, str2):
	
	# Filter bools
	if (str1 == True) or (str2 == True) or (str1 == False) or (str2 == False):
		return False

	# If either string is unconvertible to float,
	# then the 2 strings are uncomparable
	try:
		float(Fraction(str1))
		float(Fraction(str2))
		return True
	except:
		return False

