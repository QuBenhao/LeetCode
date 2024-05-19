from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 2, 3, 3, 4, 4], 3], Output=True))
		self.testcases.append(case(Input=[[5, 6, 6, 7, 8], 3], Output=False))

	def get_testcases(self):
		return self.testcases
