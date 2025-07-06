from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 5, 10], 1], Output=1))
		self.testcases.append(case(Input=[[2, 6, 8], 2], Output=1))
		self.testcases.append(case(Input=[[2, 4, 9, 6], 1], Output=2))
		self.testcases.append(case(Input=[[2,2],0], Output=2))
		self.testcases.append(case(Input=[[14,2,22],1], Output=1))
		self.testcases.append(case(Input=[[42,12,88,82,30],1], Output=2))

	def get_testcases(self):
		return self.testcases
