from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[100, 4, 200, 1, 3, 2], Output=4))
		self.testcases.append(case(Input=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1], Output=9))

	def get_testcases(self):
		return self.testcases
