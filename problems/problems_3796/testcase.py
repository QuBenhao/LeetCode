from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, [[3, 1], [8, 1]], [2, 2, 3, 1, 4, 5, 1, 1, 2]], Output=6))
		self.testcases.append(case(Input=[8, [[3, 2]], [3, 5, 2, 4, 2, 3, 1]], Output=12))

	def get_testcases(self):
		return self.testcases
