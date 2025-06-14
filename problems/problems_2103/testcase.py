from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="B0B6G0R6R0R6G9", Output=1))
		self.testcases.append(case(Input="B0R0G0R9R0B0G0", Output=1))
		self.testcases.append(case(Input="G4", Output=0))

	def get_testcases(self):
		return self.testcases
