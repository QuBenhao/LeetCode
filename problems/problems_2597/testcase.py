from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 4, 6], 2], Output=4))
		self.testcases.append(case(Input=[[1], 1], Output=1))

	def get_testcases(self):
		return self.testcases
