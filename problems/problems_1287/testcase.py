from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 2, 6, 6, 6, 6, 7, 10], Output=6))
		self.testcases.append(case(Input=[1, 1], Output=1))

	def get_testcases(self):
		return self.testcases
