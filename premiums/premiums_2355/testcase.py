from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[8, 5, 2, 7, 9], Output=19))
		self.testcases.append(case(Input=[7, 0, 3, 4, 5], Output=12))
		self.testcases.append(case(Input=[8, 2, 3, 7, 3, 4, 0, 1, 4, 3], Output=13))

	def get_testcases(self):
		return self.testcases
