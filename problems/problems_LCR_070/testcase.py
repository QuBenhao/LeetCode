from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, 2, 3, 3, 4, 4, 8, 8], Output=2))
		self.testcases.append(case(Input=[3, 3, 7, 7, 10, 11, 11], Output=10))

	def get_testcases(self):
		return self.testcases
