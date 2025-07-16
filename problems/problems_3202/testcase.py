from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4, 5], 2], Output=5))
		self.testcases.append(case(Input=[[1, 4, 2, 3, 1, 4], 3], Output=4))

	def get_testcases(self):
		return self.testcases
