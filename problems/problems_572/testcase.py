from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 4, 5, 1, 2], [4, 1, 2]], Output=True))
		self.testcases.append(case(Input=[[3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2]], Output=False))

	def get_testcases(self):
		return self.testcases
