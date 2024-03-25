from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2], [-1, 0]], Output=2))
		self.testcases.append(case(Input=[[0, 0, -1], [1, 1, 1], [2, 0, 0]], Output=4))
		self.testcases.append(case(Input=[[-1, 0], [0, 2]], Output=-1))

	def get_testcases(self):
		return self.testcases
