from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3], [3, 1, 5], [3, 2, 1]], Output=None))
		self.testcases.append(case(Input=[[1]], Output=None))

	def get_testcases(self):
		return self.testcases
