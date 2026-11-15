from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['11111222223', 3], Output="135"))
		self.testcases.append(case(Input=['00000000', 3], Output="000"))

	def get_testcases(self):
		return self.testcases
