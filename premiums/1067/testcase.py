from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, 13], Output=6))
		self.testcases.append(case(Input=[3, 100, 250], Output=35))

	def get_testcases(self):
		return self.testcases
