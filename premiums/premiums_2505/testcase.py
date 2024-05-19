from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1, 0, 3], Output=7))
		self.testcases.append(case(Input=[0, 0, 0], Output=0))

	def get_testcases(self):
		return self.testcases
