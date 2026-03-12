from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, [2, 1, 1]], Output=3))
		self.testcases.append(case(Input=[10, [3, 2, 2, 4]], Output=12))
		self.testcases.append(case(Input=[5, [1]], Output=15))

	def get_testcases(self):
		return self.testcases
