from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]]], Output=1))
		self.testcases.append(case(Input=[3, [[1, 1], [1, 2], [2, 1], [2, 2]]], Output=0))
		self.testcases.append(case(Input=[5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]], Output=1))

	def get_testcases(self):
		return self.testcases
