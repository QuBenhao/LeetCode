from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, -1], [1, 0], [2, 0], [3, 2], [4, 2]], Output=True))
		self.testcases.append(case(Input=[[0, -1], [1, 0], [2, 0], [3, 1], [4, 1]], Output=False))

	def get_testcases(self):
		return self.testcases
