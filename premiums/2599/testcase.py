from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 3, -5, 4], Output=0))
		self.testcases.append(case(Input=[3, -5, -2, 6], Output=1))

	def get_testcases(self):
		return self.testcases
