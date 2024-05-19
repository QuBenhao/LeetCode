from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[7, 4, 3, None, None, 6, 19], 3], Output=3))
		self.testcases.append(case(Input=[[7], 7], Output=7))
		self.testcases.append(case(Input=[[8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1], 4], Output=4))
		self.testcases.append(case(Input=([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), Output=5))
		self.testcases.append(case(Input=([1, 2, None, 3], 2), Output=2))

	def get_testcases(self):
		return self.testcases
