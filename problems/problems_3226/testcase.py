from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[13, 4], Output=2))
		self.testcases.append(case(Input=[21, 21], Output=0))
		self.testcases.append(case(Input=[14, 13], Output=-1))

	def get_testcases(self):
		return self.testcases
