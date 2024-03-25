from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 5], [2, 6, 3]], Output=3))
		self.testcases.append(case(Input=[[0, 1], [1, 0]], Output=4))

	def get_testcases(self):
		return self.testcases
