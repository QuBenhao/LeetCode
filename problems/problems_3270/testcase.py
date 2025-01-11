from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 10, 1000], Output=0))
		self.testcases.append(case(Input=[987, 879, 798], Output=777))
		self.testcases.append(case(Input=[1, 2, 3], Output=1))
		self.testcases.append(case(Input=[1140,1851,2057], Output=1040))

	def get_testcases(self):
		return self.testcases
