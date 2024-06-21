from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[21, 18, 18, 18, 31], [34, 32, 16, 16, 17]], Output=2))
		self.testcases.append(case(Input=[[5, 10, 16, -6, 15, 11, 3], [16, 22, 23, 23, 25, 3, -16]], Output=3))

	def get_testcases(self):
		return self.testcases
