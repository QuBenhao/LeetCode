from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 4, 6], Output=2))
		self.testcases.append(case(Input=[2, 3, 4, 7, 9], Output=2))
		self.testcases.append(case(Input=[4, 6, 5, 8], Output=3))

	def get_testcases(self):
		return self.testcases
