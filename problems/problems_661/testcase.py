from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1, 1], [1, 0, 1], [1, 1, 1]], Output=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
		self.testcases.append(case(Input=[[100, 200, 100], [200, 50, 200], [100, 200, 100]], Output=[[137, 141, 137], [141, 138, 141], [137, 141, 137]]))

	def get_testcases(self):
		return self.testcases
