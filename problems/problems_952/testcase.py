from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 6, 15, 35], Output=4))
		self.testcases.append(case(Input=[20, 50, 9, 63], Output=2))
		self.testcases.append(case(Input=[2, 3, 6, 7, 4, 12, 21, 39], Output=8))

	def get_testcases(self):
		return self.testcases
