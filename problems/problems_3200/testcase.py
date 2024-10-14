from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 4], Output=3))
		self.testcases.append(case(Input=[2, 1], Output=2))
		self.testcases.append(case(Input=[1, 1], Output=1))
		self.testcases.append(case(Input=[10, 1], Output=2))

	def get_testcases(self):
		return self.testcases
