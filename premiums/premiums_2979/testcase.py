from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 5], Output=3))
		self.testcases.append(case(Input=[5, 7], Output=23))

	def get_testcases(self):
		return self.testcases
