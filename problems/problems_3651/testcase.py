from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 3, 3], [2, 5, 4], [4, 3, 5]], 2], Output=7))
		self.testcases.append(case(Input=[[[1, 2], [2, 3], [3, 4]], 1], Output=9))

	def get_testcases(self):
		return self.testcases
