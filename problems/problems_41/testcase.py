from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 0], Output=3))
		self.testcases.append(case(Input=[3, 4, -1, 1], Output=2))
		self.testcases.append(case(Input=[7, 8, 9, 11, 12], Output=1))

	def get_testcases(self):
		return self.testcases
