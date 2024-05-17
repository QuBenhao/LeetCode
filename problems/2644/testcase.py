from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 7, 9, 3, 9], [5, 2, 3]], Output=3))
		self.testcases.append(case(Input=[[20, 14, 21, 10], [5, 7, 5]], Output=5))
		self.testcases.append(case(Input=[[12], [10, 16]], Output=10))

	def get_testcases(self):
		return self.testcases
