from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 1, 3, 3], Output=5))
		self.testcases.append(case(Input=[1, 2, 3, 4, 5], Output=0))

	def get_testcases(self):
		return self.testcases
