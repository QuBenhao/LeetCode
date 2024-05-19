from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[100, 200, 150, 1000], Output=4))
		self.testcases.append(case(Input=[900, 950, 800, 1000, 700, 800], Output=5))

	def get_testcases(self):
		return self.testcases
