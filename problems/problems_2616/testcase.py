from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 1, 2, 7, 1, 3], 2], Output=1))
		self.testcases.append(case(Input=[[4, 2, 1, 2], 1], Output=0))

	def get_testcases(self):
		return self.testcases
