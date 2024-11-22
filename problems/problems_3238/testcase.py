from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]], Output=2))
		self.testcases.append(case(Input=[5, [[1, 1], [1, 2], [1, 3], [1, 4]]], Output=0))
		self.testcases.append(case(Input=[5, [[1, 1], [2, 4], [2, 4], [2, 4]]], Output=1))

	def get_testcases(self):
		return self.testcases
