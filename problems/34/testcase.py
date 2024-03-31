from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 7, 7, 8, 8, 10], 8], Output=[3, 4]))
		self.testcases.append(case(Input=[[5, 7, 7, 8, 8, 10], 6], Output=[-1, -1]))
		self.testcases.append(case(Input=[[], 0], Output=[-1, -1]))

	def get_testcases(self):
		return self.testcases
