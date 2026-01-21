from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]], Output=3))
		self.testcases.append(case(Input=[10, [3], [3]], Output=1))
		self.testcases.append(case(Input=[100, [0, 2, 4], [4, 2, 1]], Output=1))

	def get_testcases(self):
		return self.testcases
