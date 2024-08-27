from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, [2, 3, 1, 2, 4, 3]], Output=2))
		self.testcases.append(case(Input=[4, [1, 4, 4]], Output=1))
		self.testcases.append(case(Input=[11, [1, 1, 1, 1, 1, 1, 1, 1]], Output=0))

	def get_testcases(self):
		return self.testcases
