from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]]], Output=6))
		self.testcases.append(case(Input=[4, [[1, 2, 3], [3, 4, 4]]], Output=-1))

	def get_testcases(self):
		return self.testcases
