from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3], [2]], Output=2.0))
		self.testcases.append(case(Input=[[1, 2], [3, 4]], Output=2.5))

	def get_testcases(self):
		return self.testcases
