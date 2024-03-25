from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['BSTIterator', 'next', 'next', 'prev', 'next', 'hasNext', 'next', 'next', 'next', 'hasNext', 'hasPrev', 'prev', 'prev'], [[[7, 3, 15, None, None, 9, 20]], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None], [None]]], Output=[None, 3, 7, 3, 7, True, 9, 15, 20, False, True, 15, 9]))

	def get_testcases(self):
		return self.testcases
