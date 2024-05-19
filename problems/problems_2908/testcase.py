from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[8, 6, 1, 5, 3], Output=9))
		self.testcases.append(case(Input=[5, 4, 8, 7, 10, 2], Output=13))
		self.testcases.append(case(Input=[6, 5, 4, 3, 4, 5], Output=-1))

	def get_testcases(self):
		return self.testcases
