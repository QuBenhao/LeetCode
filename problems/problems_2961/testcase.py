from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], 2], Output=[0, 2]))
		self.testcases.append(case(Input=[[[39, 3, 1000, 1000]], 17], Output=[]))

	def get_testcases(self):
		return self.testcases
