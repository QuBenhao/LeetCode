from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 5, 7], Output=[[1, 5], [7]]))
		self.testcases.append(case(Input=[2, 6, 1, 5], Output=[[2, 6], [1, 5]]))

	def get_testcases(self):
		return self.testcases
