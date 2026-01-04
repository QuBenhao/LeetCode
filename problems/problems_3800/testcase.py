from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['01000', '10111', 10, 2, 2], Output=16))
		self.testcases.append(case(Input=['001', '110', 2, 100, 100], Output=6))
		self.testcases.append(case(Input=['1010', '1010', 5, 5, 5], Output=0))

	def get_testcases(self):
		return self.testcases
