from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4, 10], 19], Output=2))
		self.testcases.append(case(Input=[[1, 4, 10, 5, 7, 19], 19], Output=1))
		self.testcases.append(case(Input=[[1, 1, 1], 20], Output=3))

	def get_testcases(self):
		return self.testcases
