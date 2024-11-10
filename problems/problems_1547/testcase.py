from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, [1, 3, 4, 5]], Output=16))
		self.testcases.append(case(Input=[9, [5, 6, 1, 4, 2]], Output=22))

	def get_testcases(self):
		return self.testcases
