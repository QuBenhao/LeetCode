from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Skiplist', 'add', 'add', 'add', 'search', 'add', 'search', 'erase', 'erase', 'search'], [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]], Output=[None, None, None, None, False, None, True, False, True, False]))

	def get_testcases(self):
		return self.testcases
