from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 2, 0, 3, 1], Output=3))
		self.testcases.append(case(Input=[1, 2, 3, 4, 0], Output=0))
		self.testcases.append(case(Input=[1, 0, 2, 4, 3], Output=2))

	def get_testcases(self):
		return self.testcases
