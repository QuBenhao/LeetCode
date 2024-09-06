from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6, 7, 8], Output=5))

	def get_testcases(self):
		return self.testcases
