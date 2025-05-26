from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 3], Output=19))
		self.testcases.append(case(Input=[5, 6], Output=15))
		self.testcases.append(case(Input=[5, 1], Output=-15))

	def get_testcases(self):
		return self.testcases
