from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 4, 3], Output=14))
		self.testcases.append(case(Input=[1, 8, 3, 5], Output=30))
		self.testcases.append(case(Input=[5], Output=0))

	def get_testcases(self):
		return self.testcases
