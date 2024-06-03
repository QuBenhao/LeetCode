from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], Output="A"))
		self.testcases.append(case(Input=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]], Output="B"))
		self.testcases.append(case(Input=[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]], Output="Draw"))

	def get_testcases(self):
		return self.testcases
