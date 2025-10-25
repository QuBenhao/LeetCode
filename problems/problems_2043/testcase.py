from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Bank', 'withdraw', 'transfer', 'deposit', 'transfer', 'withdraw'], [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]], Output=[None, True, True, True, False, False]))

	def get_testcases(self):
		return self.testcases
