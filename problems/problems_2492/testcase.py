from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]], Output=5))
		self.testcases.append(case(Input=[4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]], Output=2))

	def get_testcases(self):
		return self.testcases
