from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 2], Output=[[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]]))
		self.testcases.append(case(Input=[1, 1], Output=[[1]]))

	def get_testcases(self):
		return self.testcases
