from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 2, [1, 3], [5]], Output=13))
		self.testcases.append(case(Input=[2, 2, [7], [4]], Output=15))

	def get_testcases(self):
		return self.testcases
