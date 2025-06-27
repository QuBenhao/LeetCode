from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[6, 2, 4], Output=32))
		self.testcases.append(case(Input=[4, 11], Output=44))
		self.testcases.append(case(Input=[11,12,12], Output=276))

	def get_testcases(self):
		return self.testcases
