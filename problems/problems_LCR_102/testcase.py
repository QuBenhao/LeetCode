from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1, 1, 1, 1], 3], Output=5))
		self.testcases.append(case(Input=[[1], 1], Output=1))
		self.testcases.append(case(Input=[[43,9,26,24,39,40,20,11,18,13,14,30,48,47,37,24,32,32,2,26],47], Output=5844))

	def get_testcases(self):
		return self.testcases
