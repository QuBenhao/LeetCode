from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['10101', 1], Output=12))
		self.testcases.append(case(Input=['1010101', 2], Output=25))
		self.testcases.append(case(Input=['11111', 1], Output=15))

	def get_testcases(self):
		return self.testcases
