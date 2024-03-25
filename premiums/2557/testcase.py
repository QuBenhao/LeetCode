from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4, 6], 6, 4], Output=1))
		self.testcases.append(case(Input=[[4, 3, 5, 6], 7, 18], Output=3))

	def get_testcases(self):
		return self.testcases
