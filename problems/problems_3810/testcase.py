from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3], [2, 1, 3]], Output=2))
		self.testcases.append(case(Input=[[4, 1, 4], [5, 1, 4]], Output=1))
		self.testcases.append(case(Input=[[7, 3, 7], [5, 5, 9]], Output=2))

	def get_testcases(self):
		return self.testcases
