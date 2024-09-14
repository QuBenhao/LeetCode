from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 6], [1, 5], [4, 7]], Output=7))
		self.testcases.append(case(Input=[[1, 3], [5, 8]], Output=7))

	def get_testcases(self):
		return self.testcases
