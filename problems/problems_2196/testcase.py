from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]], Output=[50, 20, 80, 15, 17, 19]))
		self.testcases.append(case(Input=[[1, 2, 1], [2, 3, 0], [3, 4, 1]], Output=[1, 2, None, None, 3, 4]))

	def get_testcases(self):
		return self.testcases
