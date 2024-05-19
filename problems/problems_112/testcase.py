from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22], Output=True))
		self.testcases.append(case(Input=[[1, 2, 3], 5], Output=False))
		self.testcases.append(case(Input=[[], 0], Output=False))

	def get_testcases(self):
		return self.testcases
