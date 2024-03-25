from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1, 4], [1, 0, 3], 5], Output=True))
		self.testcases.append(case(Input=[[0, -10, 10], [5, 1, 7, 0, 2], 18], Output=False))

	def get_testcases(self):
		return self.testcases
