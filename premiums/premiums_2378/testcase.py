from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[-1, -1], [0, 5], [0, 10], [2, 6], [2, 4]], Output=11))
		self.testcases.append(case(Input=[[-1, -1], [0, 5], [0, -6], [0, 7]], Output=7))

	def get_testcases(self):
		return self.testcases
