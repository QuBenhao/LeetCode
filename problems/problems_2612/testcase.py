from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 0, [1, 2], 4], Output=[0, -1, -1, 1]))
		self.testcases.append(case(Input=[5, 0, [2, 4], 3], Output=[0, -1, -1, -1, -1]))
		self.testcases.append(case(Input=[4, 2, [0, 1, 3], 1], Output=[-1, -1, 0, -1]))

	def get_testcases(self):
		return self.testcases
