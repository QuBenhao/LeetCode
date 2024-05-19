from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1], Output=1))
		self.testcases.append(case(Input=[5, 5], Output=4))

	def get_testcases(self):
		return self.testcases
