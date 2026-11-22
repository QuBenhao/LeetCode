from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['ProductOfNumbers', 'add', 'add', 'add', 'add', 'add', 'getProduct', 'getProduct', 'getProduct', 'add', 'getProduct'], [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]], Output=[None, None, None, None, None, None, 20, 40, 0, None, 32]))

	def get_testcases(self):
		return self.testcases
