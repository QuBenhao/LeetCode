from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['10110101', 2, 2], Output=2))
		self.testcases.append(case(Input=['11111', 2, 3], Output=0))

	def get_testcases(self):
		return self.testcases
