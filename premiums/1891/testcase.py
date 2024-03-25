from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[9, 7, 5], 3], Output=5))
		self.testcases.append(case(Input=[[7, 5, 9], 4], Output=4))
		self.testcases.append(case(Input=[[5, 7, 9], 22], Output=0))

	def get_testcases(self):
		return self.testcases
