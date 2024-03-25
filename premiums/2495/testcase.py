from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[9, 6, 7, 13], Output=6))
		self.testcases.append(case(Input=[7, 3, 5], Output=0))

	def get_testcases(self):
		return self.testcases
