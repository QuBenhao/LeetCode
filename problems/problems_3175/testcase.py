from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 2, 6, 3, 9], 2], Output=2))
		self.testcases.append(case(Input=[[2, 5, 4], 3], Output=1))
		self.testcases.append(case(Input=[[4,18,17,20,15,12,8,5],1], Output=1))

	def get_testcases(self):
		return self.testcases
