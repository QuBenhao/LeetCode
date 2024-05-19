from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 0, 0, 2, 3], [0, 3, 0, 4, 0]], Output=8))
		self.testcases.append(case(Input=[[0, 1, 0, 0, 0], [0, 0, 0, 0, 2]], Output=0))
		self.testcases.append(case(Input=[[0, 1, 0, 0, 2, 0, 0], [1, 0, 0, 0, 3, 0, 4]], Output=6))

	def get_testcases(self):
		return self.testcases
