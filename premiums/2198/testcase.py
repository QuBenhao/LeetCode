from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 6, 7, 3, 2], Output=12))
		self.testcases.append(case(Input=[1, 2, 2], Output=6))
		self.testcases.append(case(Input=[1, 1, 1], Output=0))

	def get_testcases(self):
		return self.testcases
