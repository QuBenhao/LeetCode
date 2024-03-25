from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1], 1], Output=1))
		self.testcases.append(case(Input=[[1, 2], 5], Output=7))
		self.testcases.append(case(Input=[[1, 2, 3], 1], Output=4))

	def get_testcases(self):
		return self.testcases
