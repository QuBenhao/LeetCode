from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, [[2, 3], [1, 4]]], Output=9))
		self.testcases.append(case(Input=[5, [[1, 2], [2, 5], [3, 5]]], Output=12))

	def get_testcases(self):
		return self.testcases
