from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['aaabcbbcc', 3], Output=3))
		self.testcases.append(case(Input=['abcd', 2], Output=0))
		self.testcases.append(case(Input=['a', 5], Output=0))

	def get_testcases(self):
		return self.testcases
