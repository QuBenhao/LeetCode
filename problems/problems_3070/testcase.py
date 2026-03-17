from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[7, 6, 3], [6, 6, 1]], 18], Output=4))
		self.testcases.append(case(Input=[[[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20], Output=6))

	def get_testcases(self):
		return self.testcases
