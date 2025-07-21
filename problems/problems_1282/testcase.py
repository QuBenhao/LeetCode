from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 3, 3, 3, 3, 1, 3], Output=[[5], [0, 1, 2], [3, 4, 6]]))
		self.testcases.append(case(Input=[2, 1, 3, 3, 3, 2], Output=[[1], [0, 5], [2, 3, 4]]))

	def get_testcases(self):
		return self.testcases
