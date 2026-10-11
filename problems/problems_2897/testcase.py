from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 6, 5, 8], 2], Output=261))
		self.testcases.append(case(Input=[[4, 5, 4, 7], 3], Output=90))

	def get_testcases(self):
		return self.testcases
