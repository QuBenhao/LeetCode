from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 3, 1, 7], [1, 3, 2, 4], 1], Output=[0, -1, 2, -1]))
		self.testcases.append(case(Input=[[1, 2, 3], [10], 5], Output=[-1]))

	def get_testcases(self):
		return self.testcases
