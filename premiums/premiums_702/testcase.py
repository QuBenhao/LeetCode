from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[-1, 0, 3, 5, 9, 12], 9], Output=4))
		self.testcases.append(case(Input=[[-1, 0, 3, 5, 9, 12], 2], Output=-1))

	def get_testcases(self):
		return self.testcases
