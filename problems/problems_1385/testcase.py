from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 5, 8], [10, 9, 1, 8], 2], Output=2))
		self.testcases.append(case(Input=[[1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3], Output=2))
		self.testcases.append(case(Input=[[2, 1, 100, 3], [-5, -2, 10, -3, 7], 6], Output=1))

	def get_testcases(self):
		return self.testcases
