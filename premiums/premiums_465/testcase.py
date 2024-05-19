from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, 10], [2, 0, 5]], Output=2))
		self.testcases.append(case(Input=[[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]], Output=1))

	def get_testcases(self):
		return self.testcases
