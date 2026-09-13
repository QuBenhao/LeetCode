from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 0, 2, 2], [1, 1, 3, 3]], Output=True))
		self.testcases.append(case(Input=[[0, 0, 1, 1], [1, 0, 2, 1]], Output=False))
		self.testcases.append(case(Input=[[0, 0, 1, 1], [2, 2, 3, 3]], Output=False))

	def get_testcases(self):
		return self.testcases
