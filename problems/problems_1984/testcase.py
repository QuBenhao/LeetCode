from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[90], 1], Output=0))
		self.testcases.append(case(Input=[[9, 4, 1, 7], 2], Output=2))

	def get_testcases(self):
		return self.testcases
