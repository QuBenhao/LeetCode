from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[13, 2], Output=10))
		self.testcases.append(case(Input=[1, 1], Output=1))
		self.testcases.append(case(Input=[10, 3], Output=2))
		self.testcases.append(case(Input=[681692778,351251360], Output=416126219))

	def get_testcases(self):
		return self.testcases
