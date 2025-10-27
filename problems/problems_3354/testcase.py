from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 0, 2, 0, 3], Output=2))
		self.testcases.append(case(Input=[2, 3, 4, 0, 4, 1, 0], Output=0))

	def get_testcases(self):
		return self.testcases
