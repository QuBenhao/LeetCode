from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=0, Output=[[0]]))
		self.testcases.append(case(Input=1, Output=[[3, 0], [2, 1]]))
		self.testcases.append(case(Input=2, Output=[[15, 12, 3, 0], [14, 13, 2, 1], [11, 8, 7, 4], [10, 9, 6, 5]]))

	def get_testcases(self):
		return self.testcases
