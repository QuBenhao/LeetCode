from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 7, 3, 9, 4, 9, 8, 3, 1], Output=8))
		self.testcases.append(case(Input=[9, 9, 8, 8], Output=-1))

	def get_testcases(self):
		return self.testcases
