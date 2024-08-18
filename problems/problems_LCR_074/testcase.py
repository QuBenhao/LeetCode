from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3], [2, 6], [8, 10], [15, 18]], Output=[[1, 6], [8, 10], [15, 18]]))

	def get_testcases(self):
		return self.testcases
