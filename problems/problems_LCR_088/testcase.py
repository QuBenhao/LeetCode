from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 15, 20], Output=15))
		self.testcases.append(case(Input=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], Output=6))

	def get_testcases(self):
		return self.testcases
