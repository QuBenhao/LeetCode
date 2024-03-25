from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[5, 4, 6], 1], Output=5))
		self.testcases.append(case(Input=[[2, 3, 5, 8], 5], Output=12))
		self.testcases.append(case(Input=[[10, 5, 9, 11], 20], Output=16))

	def get_testcases(self):
		return self.testcases
