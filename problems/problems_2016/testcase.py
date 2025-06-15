from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, 1, 5, 4], Output=4))
		self.testcases.append(case(Input=[9, 4, 3, 2], Output=-1))
		self.testcases.append(case(Input=[1, 5, 2, 10], Output=9))

	def get_testcases(self):
		return self.testcases
