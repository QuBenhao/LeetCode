from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Vector2D', 'next', 'next', 'next', 'hasNext', 'hasNext', 'next', 'hasNext'], [[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]], Output=[None, 1, 2, 3, True, True, 4, False]))

	def get_testcases(self):
		return self.testcases
