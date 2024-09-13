from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[8, [4, 1, 8, 4, 5], [5, 6, 1, 8, 4, 5], 2, 3], Output=8))

	def get_testcases(self):
		return self.testcases
