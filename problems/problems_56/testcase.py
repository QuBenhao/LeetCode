from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3], [2, 6], [8, 10], [15, 18]], Output=[[1, 6], [8, 10], [15, 18]]))
		self.testcases.append(case(Input=[[1, 4], [4, 5]], Output=[[1, 5]]))

	def get_testcases(self):
		return self.testcases
