from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 5, 2, 6], 100], Output=8))
		self.testcases.append(case(Input=[[1, 2, 3], 0], Output=0))

	def get_testcases(self):
		return self.testcases
