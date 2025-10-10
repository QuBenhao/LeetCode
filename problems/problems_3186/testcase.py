from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, 3, 4], Output=6))
		self.testcases.append(case(Input=[7, 1, 6, 6], Output=13))

	def get_testcases(self):
		return self.testcases
