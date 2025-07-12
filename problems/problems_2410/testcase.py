from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4, 7, 9], [8, 2, 5, 8]], Output=2))
		self.testcases.append(case(Input=[[1, 1, 1], [10]], Output=1))

	def get_testcases(self):
		return self.testcases
