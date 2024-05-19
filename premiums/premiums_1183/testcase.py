from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 3, 2, 1], Output=4))
		self.testcases.append(case(Input=[3, 3, 2, 2], Output=6))

	def get_testcases(self):
		return self.testcases
