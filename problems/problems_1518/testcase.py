from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[9, 3], Output=13))
		self.testcases.append(case(Input=[15, 4], Output=19))

	def get_testcases(self):
		return self.testcases
