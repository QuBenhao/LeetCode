from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['11', '1'], Output="100"))
		self.testcases.append(case(Input=['11', '10'], Output="101"))
		self.testcases.append(case(Input=['1010', '1011'], Output="10101"))

	def get_testcases(self):
		return self.testcases
