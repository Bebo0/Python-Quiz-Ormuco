from fractions import Fraction
"""Compares 2 string to see if they're numbers

"""
def comparable(str1, str2):

	# Filter out bools because bools are considered floats
	if isinstance(str1, bool) or isinstance(str2, bool):
		return False

	# If either string is unconvertible to float,
	# then the 2 strings are uncomparable
	try:
		float(Fraction(str1))
		float(Fraction(str2))
		return True
	except:
		return False

