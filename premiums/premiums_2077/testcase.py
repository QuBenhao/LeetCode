from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[1, 2], [5, 2], [4, 1], [2, 4], [3, 1], [3, 4]]], Output=2))
		self.testcases.append(case(Input=[4, [[1, 2], [3, 4]]], Output=0))

	def get_testcases(self):
		return self.testcases
