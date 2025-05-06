from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['BSTIterator', 'next', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext', 'next', 'hasNext'], [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]], Output=[None, 3, 7, True, 9, True, 15, True, 20, False]))

	def get_testcases(self):
		return self.testcases
