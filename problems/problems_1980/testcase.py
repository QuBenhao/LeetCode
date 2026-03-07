from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['01', '10'], Output="11"))
		self.testcases.append(case(Input=['00', '01'], Output="11"))
		self.testcases.append(case(Input=['111', '011', '001'], Output="101"))

	def get_testcases(self):
		return self.testcases
