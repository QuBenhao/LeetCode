from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[6, 2], [2, 6], [3, 4]], 9], Output=4))
		self.testcases.append(case(Input=[[[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8], Output=10))

	def get_testcases(self):
		return self.testcases
