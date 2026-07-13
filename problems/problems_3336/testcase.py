from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=10))
		self.testcases.append(case(Input=[10, 20, 30], Output=2))
		self.testcases.append(case(Input=[1, 1, 1, 1], Output=50))

	def get_testcases(self):
		return self.testcases
