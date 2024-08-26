from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3], Output=1))
		self.testcases.append(case(Input=[3, 4, 3, 4, 5], Output=2))
		self.testcases.append(case(Input=[4, 3, 5, 4], Output=2))

	def get_testcases(self):
		return self.testcases
