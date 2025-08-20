from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4, None, 2, 4, None, None, 4], Output=[[2, 4], [4]]))
		self.testcases.append(case(Input=[2, 1, 1], Output=[[1]]))
		self.testcases.append(case(Input=[2, 2, 2, 3, None, 3, None], Output=[[2, 3], [3]]))

	def get_testcases(self):
		return self.testcases
