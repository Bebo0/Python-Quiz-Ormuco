import unittest
from questionA import Line, overlap

from questionB.questionB import comparable

from questionC.questionC import GDLRUC

class TestQuestionA(unittest.TestCase):

	def test_overlap(self):
		line1 = Line(1,5)
		line2 = Line(2,6)
		line3 = Line(6,8)
		self.assertTrue(overlap(line1,line2))
		self.assertFalse(overlap(line1,line3))

class TestQuestionB(unittest.TestCase):

	def test_comparable_regular(self):
		str1 = "1.1"
		str2 = "1.2"
		self.assertTrue(comparable(str1,str2))

	def test_comparable_int(self):
		str1 = "1"
		str2 = "2"
		self.assertTrue(comparable(str1,str2))

	def test_comparable_negatives(self):
		str1 = "-1.1"
		str2 = "1.2"
		self.assertTrue(comparable(str1,str2))

	def test_comparable_fractions(self):
		str1 = "1/3"
		str2 = "1/4"
		self.assertTrue(comparable(str1,str2))

	def test_comparable_negative_fractions(self):
		str1 = "1/3"
		str2 = "-1/4"
		self.assertTrue(comparable(str1,str2))

	def test_comparable_string(self):
		str1 = "hello world"
		str2 = "1.2"
		self.assertFalse(comparable(str1,str2))

	def test_comparable_bool(self):
		str1 = True
		str2 = "1.2"
		self.assertFalse(comparable(str1,str2))


class TestQuestionC(unittest.TestCase):
	
	def test_cache_get(self):
		testCache = GDLRUC(2)
		testCache.set("hello world", "hello back")
		testCache.set("foo", "bar")
		self.assertEqual(testCache.get("hello world"), "hello back")

	def test_cache_remove_and_set(self):
		testCache = GDLRUC(2)
		testCache.set("hello world", "hello back")
		testCache.set("foo", "bar")
		testCache.set("ada", "lovelace")
		self.assertEqual(testCache.get("hello world"), -1)

	def test_cache_update_order(self):
		testCache = GDLRUC(2)
		testCache.set("hello world", "hello back")
		testCache.set("foo", "bar")
		testCache.get("hello world")
		testCache.set("ada", "lovelace")
		self.assertEqual(testCache.get("hello world"), "hello back")
		self.assertEqual(testCache.get("foo"), -1)


if __name__ == '__main__':
	unittest.main()