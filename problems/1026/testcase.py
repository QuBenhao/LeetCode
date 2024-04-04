from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13], Output=7))
		self.testcases.append(case(Input=[1, None, 2, None, 0, 3], Output=3))

	def get_testcases(self):
		return self.testcases
