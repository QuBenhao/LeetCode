from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 4, 5, 5, 3, 1], Output=6))
		self.testcases.append(case(Input=[9], Output=0))

	def get_testcases(self):
		return self.testcases
