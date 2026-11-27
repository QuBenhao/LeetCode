from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 6], [2, 4], [3, 5]], 19], Output=5))
		self.testcases.append(case(Input=[[[2, 8], [1, 10], [6, 6], [4, 12], [5, 20], [5, 17]], 35], Output=7))

	def get_testcases(self):
		return self.testcases
