import unittest
from questionA import Line, overlap

class TestQuestionA(unittest.TestCase):

	def test_overlap(self):
		line1 = Line(1,5)
		line2 = Line(2,6)
		line3 = Line(6,8)
		self.assertTrue(overlap(line1,line2))
		self.assertFalse(overlap(line1,line3))

if __name__ == '__main__':
	unittest.main()