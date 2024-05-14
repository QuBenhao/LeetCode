from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4], Output=4))
		self.testcases.append(case(Input=[2, 3, 3], Output=-1))

	def get_testcases(self):
		return self.testcases
