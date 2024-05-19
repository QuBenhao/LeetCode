from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]], Output=100))
		self.testcases.append(case(Input=[[85, 47, 57], [24, 66, 99], [40, 25, 25]], Output=0))

	def get_testcases(self):
		return self.testcases
