from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 0, 1], Output=2))
		self.testcases.append(case(Input=[9, 6, 4, 2, 3, 5, 7, 0, 1], Output=8))

	def get_testcases(self):
		return self.testcases
