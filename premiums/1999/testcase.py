from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 0, 2], Output=20))
		self.testcases.append(case(Input=[3, 4, 2], Output=24))
		self.testcases.append(case(Input=[2, 0, 0], Output=-1))

	def get_testcases(self):
		return self.testcases
