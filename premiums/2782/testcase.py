from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[6, [1, 1, 2, 2, 3, 3]], Output=3))
		self.testcases.append(case(Input=[5, [1, 2, 3, 4, 5]], Output=5))
		self.testcases.append(case(Input=[3, [1, 1, 1]], Output=1))

	def get_testcases(self):
		return self.testcases
