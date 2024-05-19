from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1992, 7], Output=31))
		self.testcases.append(case(Input=[2000, 2], Output=29))
		self.testcases.append(case(Input=[1900, 2], Output=28))

	def get_testcases(self):
		return self.testcases
